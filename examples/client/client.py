import asyncio
from fastmcp import Client, FastMCP

client = Client("http://127.0.0.1:8080/mcp/")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print("# Tools\n\n", tools, "\n\n")
        resources = await client.list_resources()
        print("# Resources\n\n", resources, "\n\n")
        prompts = await client.list_prompts()
        print("# Prompts\n\n", prompts, "\n\n")
        
        # Execute operations
        result = await client.call_tool("ask_chatgpt", {"request": "What is AI?"})
        #print(result, "\n\n")
        print(result.content[0].text, "\n\n")

        result = await client.get_prompt("ask_multiple_models", {"request": "What is AI?"})
        #print(result, "\n\n")
        print(result.messages[0].content.text)


asyncio.run(main())
