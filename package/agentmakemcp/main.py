from agentmake import readTextFile
from agentmakemcp import compileServerScripts
import os, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("default", default=None, help="AgentMake AI MCP server configuration file path.")
    args = parser.parse_args()

    if args.default is None:
        print("Error! You need to specify an AgentMake AI MCP server configuration file path, e.g. `examples/youtube_utilities.py`")
        exit(1)

    filepath = args.default
    if os.path.isfile(filepath):
        configs = readTextFile(filepath)
        if configs:
            configs = eval(configs)
            if isinstance(configs, dict):
                exec(compileServerScripts(configs))
            else:
                print("Error! Invalid config file! Read instructions at: https://github.com/eliranwong/agentmakemcp")
                exit(1)
    else:
        print(f"Error! File `{filepath}` does not exist!")
        exit(1)


if __name__ == "__main__":
    main()