{
    "server": "Different Persona",
    "transport": "http",
    "port": 8081,
    "settings": [
        # add three mcp tools
        {
            "name": "ask_narrative_therapist",
            "description": "Ask a narrative therapist",
            "agentmake": {"system": "counsellors/Narrative_Therapy"},
        },
        {
            "name": "ask_family_systems_therapist",
            "description": "Ask a family systems therapist",
            "agentmake": {"system": "counsellors/Family_Systems_Therapy"},
        },
        {
            "name": "ask_church_pastor",
            "description": "Ask a church pastor",
            "agentmake": {"system": "bible/billy"},
        },
    ]
}