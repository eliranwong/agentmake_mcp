# Bible Study System Configuration
{
    "server": "Bible Study",
    "transport": "http",
    "port": 8084,
    "settings": [
        # add multiple mcp tools
        # AgentMake AI tools for Bible Study
        {
            "name": "compare_bible_translations",
            "description": "compare Bible translations; bible verse reference(s) must be given",
            "agentmake": {"tool": "uba/compare"},
        },
        {
            "name": "retrieve_bible_study_indexes",
            "description": "retrieve smart indexes on studying a particular bible verse; bible verse reference must be given",
            "agentmake": {"tool": "uba/index"},
        },
        {
            "name": "retrieve_bible_cross_references",
            "description": "retrieve cross-references of Bible verses; bible verse reference(s) must be given",
            "agentmake": {"tool": "uba/xref"},
        },
        {
            "name": "retrieve_english_bible_verses",
            "description": "retrieve English Bible verses; bible verse reference(s) must be given",
            "agentmake": {"tool": "uba/net"},
        },
        {
            "name": "search_bible_or_run_uba_command",
            "description": "search the bible; run UniqueBible App UBA command; either search string or full command must be given",
            "agentmake": {"tool": "uba/cmd"},
        },
        {
            "name": "read_bible_commentary",
            "description": "read bible commentary; bible verse reference(s) must be given",
            "agentmake": {"tool": "uba/comment"},
        },
        {
            "name": "retrieve_chinese_bible_verses",
            "description": "retrieve Chinese Bible verses; bible verse reference(s) must be given",
            "agentmake": {"tool": "uba/cuv"},
        },
        # AgentMake AI systems for Bible Study
        {
            "name": "refine_bible_translation",
            "description": "refine the translation of a Bible verse or passage",
            "agentmake": {"system": "bible/translate"},
        },
        {
            "name": "write_pastor_prayer",
            "description": "write a prayer, out of a church pastor heart, based on user input",
            "agentmake": {"system": "bible/pray"},
        },
        {
            "name": "ask_theologian",
            "description": "ask a theologian about the bible",
            "agentmake": {"system": "bible/theologian"},
        },
        {
            "name": "quote_bible_verses",
            "description": "quote multiple bible verses in response to user request",
            "agentmake": {"system": "bible/quote"},
        },
        {
            "name": "anyalyze_psalms",
            "description": "analyze the context and background of the Psalms in the bible",
            "agentmake": {"system": "bible/david"},
        },
        {
            "name": "ask_pastor",
            "description": "ask a church pastor about the bible",
            "agentmake": {"system": "bible/billy"},
        },
        {
            "name": "ask_bible_scholar",
            "description": "ask a bible scholar about the bible",
            "agentmake": {"system": "bible/scholar"},
        },
        # AgentMake AI instructions for Bible Study
        {
            "name": "explain_bible_meaning",
            "description": "Explain the meaning of the user-given content in reference to the Bible",
            "agentmake": {"instruction": "bible/meaning", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_new testament_historical_context",
            "description": "write the Bible Historical Context of a New Testament passage in the bible; new testament bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/nt_context", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_questions",
            "description": "Write thought-provoking questions for bible study group discussion; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/questions", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_devotion",
            "description": "Write a devotion on a bible passage; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/devotion", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "translate_hebrew_bible_verse",
            "description": "Translate a Hebrew bible verse; Hebrew bible text must be given",
            "agentmake": {"instruction": "bible/translate_hebrew", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_location_study",
            "description": "write comprehensive information on a bible location; a bible location name must be given",
            "agentmake": {"instruction": "bible/location", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "translate_greek_bible_verse",
            "description": "Translate a Greek bible verse: Greek bible text must be given",
            "agentmake": {"instruction": "bible/translate_greek", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "identify_bible_keywords",
            "description": "Identify bible key words from the user-given content",
            "agentmake": {"instruction": "bible/keywords", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "study_old_testament_themes",
            "description": "Study Bible Themes in a Old Testament passage; old testatment bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/ot_themes", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "study_new_testament_themes",
            "description": "Study Bible Themes in a New Testament passage; new testament bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/nt_themes", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_old_testament_highlights",
            "description": "Write Highlights in a Old Testament passage in the bible; old testament bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/ot_highligths", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_prayer",
            "description": "Write a prayer pertaining to the user content in reference to the Bible",
            "agentmake": {"instruction": "bible/prayer", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_short_bible_prayer",
            "description": "Write a short prayer, in one paragraph only, pertaining to the user content in reference to the Bible",
            "agentmake": {"instruction": "bible/short_prayer", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_character_study",
            "description": "Write comprehensive information on a given bible character in the bible; a bible character name must be given",
            "agentmake": {"instruction": "bible/character", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_thought_progression",
            "description": "write Bible Thought Progression of a bible book / chapter / passage; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/flow", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "quote_bible_promises",
            "description": "Quote relevant Bible promises in response to user request",
            "agentmake": {"instruction": "bible/promises", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_chapter_summary",
            "description": "Write a detailed interpretation on a bible chapter; a bible chapter must be given",
            "agentmake": {"instruction": "bible/chapter_summary", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_perspectives",
            "description": "Write biblical perspectives and principles in relation to the user content",
            "agentmake": {"instruction": "bible/perspective", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "interpret_old_testament_verse",
            "description": "Interpret the user-given bible verse from the Old Testament in the light of its context, together with insights of biblical Hebrew studies; an old testament bible verse / reference(s) must be given",
            "agentmake": {"instruction": "bible/ot_meaning", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "expound_bible_topic",
            "description": "Expound the user-given topic in reference to the Bible; a topic must be given",
            "agentmake": {"instruction": "bible/topic", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_theology",
            "description": "write the theological messages conveyed in the user-given content, in reference to the Bible",
            "agentmake": {"instruction": "bible/theology", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "study_bible_themes",
            "description": "Study Bible Themes in relation to the user content",
            "agentmake": {"instruction": "bible/themes", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_canonical_context",
            "description": "Write about canonical context of a bible book / chapter / passage; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/canon", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_related_summary",
            "description": "Write a summary on the user-given content in reference to the Bible",
            "agentmake": {"instruction": "bible/summary", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "interpret_new_testament_verse",
            "description": "Interpret the user-given bible verse from the New Testament in the light of its context, together with insights of biblical Greek studies; a new testament bible verse / reference(s) must be given",
            "agentmake": {"instruction": "bible/nt_meaning", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_new_testament_highlights",
            "description": "Write Highlights in a New Testament passage in the bible; new testament bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/nt_highlights", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_applications",
            "description": "Provide detailed applications of a bible passages; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/application", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_book_introduction",
            "description": "Write a detailed introduction on a book in the bible; bible book must be given",
            "agentmake": {"instruction": "bible/introduce_book", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_old testament_historical_context",
            "description": "write the Bible Historical Context of a Old Testament passage in the bible; old testament bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/ot_context", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_outline",
            "description": "provide a detailed outline of a bible book / chapter / passage; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/outline", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_insights",
            "description": "Write exegetical insights in detail on a bible passage; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/insights", "system": "auto", "backend": "googleai"},
        },
        {
            "name": "write_bible_sermon",
            "description": "Write a bible sermon based on a bible passage; bible book / chapter / passage / reference(s) must be given",
            "agentmake": {"instruction": "bible/sermon", "system": "auto", "backend": "googleai"},
        },
    ]
}