{
    "server": "Teamwork and Toolmate AI",
    "transport": "http",
    "port": 8082,
    "settings": [
        # add two agents as two mcp tools
        {
            "name": "Teamwork AI",
            "description": "Use Teamwork AI to process a written task request by a team of AI agents.",
            "agentmake": {"backend": "azure", "agent": "teamwork"},
        },
        {
            "name": "ToolMate AI",
            "description": "Use ToolMate AI agent to execute a task.",
            "agentmake": {"backend": "genai", "agent": "toolmate"},
        },
    ]
}