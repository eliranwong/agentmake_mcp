from agentmake import DEVELOPER_MODE, USER_OS, AGENTMAKE_USER_DIR, PACKAGE_PATH, readTextFile, writeTextFile
from pathlib import Path
import os, traceback, re


def readToolFile(tool_object: str) -> set:
    """return tool description and parameters"""
    tool_name = tool_object[:20]
    if USER_OS == "Windows":
        tool_object = os.path.join(*tool_object.split("/"))
    possible_tool_file_path_2 = os.path.join(PACKAGE_PATH, "tools", f"{tool_object}.py")
    possible_tool_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "tools", f"{tool_object}.py")
    if tool_object is None:
        pass
    elif os.path.isfile(possible_tool_file_path_1):
        tool_file_content = readTextFile(possible_tool_file_path_1)
        if tool_file_content:
            tool_object = tool_file_content
    elif os.path.isfile(possible_tool_file_path_2):
        tool_file_content = readTextFile(possible_tool_file_path_2)
        if tool_file_content:
            tool_object = tool_file_content
    elif os.path.isfile(tool_object): # tool_object itself is a valid filepath
        tool_file_content = readTextFile(tool_object)
        if tool_file_content:
            tool_object = tool_file_content
    if tool_object:
        glob = {}
        loc = {}
        try:
            exec(tool_object, glob, loc)
            schema = loc.get("TOOL_SCHEMA")
            description = description = schema["description"] if schema else loc.get("TOOL_DESCRIPTION", "")
            parameters = schema["parameters"] if schema and "parameters" in schema else {}
            return description, parameters
        except Exception as e:
            print(f"Failed to execute tool `{tool_name}`! An error occurred: {e}")
            if DEVELOPER_MODE:
                print(traceback.format_exc())
    return "", {}

def compileServerScripts(configs: dict) -> str:
    scripts = []
    ob, cb = "{", "}"
    server = configs.get("server", "AgentMake AI")
    port = configs.get("port", 8080)
    transport = configs.get("transport", "http")

    for i in configs["settings"]:
        if "agentmake" in i:
            am = i["agentmake"]

            if isinstance(am, str): # add a mcp prompt
                # add to server script
                script = f"""@mcp.prompt
def {i["name"].replace(" ", "_").lower()}(request:str) -> PromptMessage:
    \"\"\"{i["description"]}\"\"\"
    global logger, PromptMessage, TextContent
    logger.info(f"[Request] {ob}request{cb}")
    prompt_text = f\"\"\"{am}

# Here is the request:
---
{ob}request{cb}
---
\"\"\"
    return PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))"""
                scripts.append(script)

            elif isinstance(am, dict): # add a mcp tool
                # fill in tool name and description when a tool is specified
                if not "agent" in am and "tool" in am and am["tool"]:
                    firstTool = am["tool"] if isinstance(am["tool"], str) else am["tool"][0]
                    if not "name" in i:
                        i["name"] = firstTool.replace("/", "_")
                    description, parameters = readToolFile(firstTool)
                    if not "description" in i:
                        i["description"] = description
                    # specify tool arguments in tool description
                    if parameters and not re.search(r"^Args \[", description):
                        required = parameters["required"]
                        optional = [o for o in parameters["properties"] if not o in required]
                        if required:
                            args = [f"{r}: {parameters["properties"][r]['description']}" for r in required]
                            args = "\n    ".join(args)
                            i["description"] += f"""

Args [required]:
    {args}
"""
                        if optional:
                            args = [f"{o}: {parameters["properties"][o]['description']}" for o in optional]
                            args = "\n    ".join(args)
                            i["description"] += f"""
Args [optional]:
    {args}
"""

                # check name and description
                if not "name" in i:
                    print(f"Error! Parameter `name` is missing in item {i}!")
                    exit(1)
                elif not "description" in i:
                    print(f"Error! Parameter `description` is missing in item {i}!")
                    exit(1)
                
                # add to server script
                am["print_on_terminal"] = False
                am["word_wrap"] = False
                script = f"""@mcp.tool
def {i["name"].replace(" ", "_").lower()}(request:str) -> str:
    \"\"\"{i["description"]}\"\"\"
    global logger, agentmake, getResponse
    logger.info(f"[Request] {ob}request{cb}")
    messages = agentmake(request, **{am})
    return getResponse(messages)"""
                scripts.append(script)

    mcp_server_script = f"""from fastmcp import FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent
from agentmake import agentmake
import logging, os

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP(name="{server}")

def getResponse(messages:list) -> str:
    return messages[-1].get("content") if messages and "content" in messages[-1] else "Error!"

""" + "\n\n".join(scripts) + f"""

logger.info(f"MCP server `{server}` started on port {port}")
mcp.run(transport="{transport}", port={port})"""

    # back up mcp server script
    folderPath = os.path.join(AGENTMAKE_USER_DIR, "mcp")
    Path(folderPath).mkdir(parents=True, exist_ok=True)
    filePath = os.path.join(folderPath, f"{server.replace(' ', '_')}.py")
    writeTextFile(filePath, mcp_server_script)
    print(f"\n# Backup\n\nAgentMake MCP Server script was generated and saved to: {filePath}\n")

    # setup hints
    print(f"""# Starting MCP server `{server}` on port `{port}` ...

# Integration with Other AI Tools
          
For example, to work with `Gemini CLI`, add the following block: in `~/.gemini/settings.json`:
          
{ob}
  ...
  "mcpServers": {ob}
    "{server}": {ob}
      "httpUrl": "http://127.0.0.1:{port}/mcp/"
    {cb}
  {cb}
{cb}
""")

    return mcp_server_script
