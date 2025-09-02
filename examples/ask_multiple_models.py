{
    "server": "Ask Multiple AI Models",
    "transport": "http",
    "port": 8080,
    "settings": [
        # add four mcp tools
        {
            "name": "ask_chatgpt",
            "description": "Ask ChatGPT",
            "agentmake": {"backend": "azure", "model": "gpt-5-chat"},
        },
        {
            "name": "ask_grok",
            "description": "Ask Grok",
            "agentmake": {"backend": "grok", "model": "grok-3"},
        },
        {
            "name": "ask_claude",
            "description": "Ask Claude",
            "agentmake": {"backend": "anthropic", "model": "claude-3-5-sonnet-latest"},
        },
        {
            "name": "ask_gemini",
            "description": "Ask Gemini",
            "agentmake": {"backend": "genai", "model": "gemini-2.5-pro"},
        },
        # add a mcp prompt
        {
            "name": "ask_multiple_models",
            "description": "Ask multiple AI models at once",
            "agentmake": """You are a moderator in a collaborative discussion. Your goal is to pass the original request to different AI models for reviews and summarize the results.
    
Please perform the following steps in order:
1. Call the tool `ask_chatgpt` to answer the request.
2. Call the tool `ask_grok` to answer the request.
3. Call the tool `ask_claude` to answer the request.
4. Call the tool `ask_gemini` to answer the request.
5. Compare the reviews.
6. Summarize the results.
"""
        },
    ]
}