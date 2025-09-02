import asyncio
from fastmcp import Client, FastMCP

# HTTP server
client = Client("http://127.0.0.1:8080/mcp/")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print("# Tools\n\n", tools)
        resources = await client.list_resources()
        print("# Resources\n\n", resources)
        prompts = await client.list_prompts()
        print("# Prompts\n\n", prompts)
        
        # Execute operations
        result = await client.call_tool("ask_chatgpt", {"request": "What is AI?"})
        print(result)

asyncio.run(main())
