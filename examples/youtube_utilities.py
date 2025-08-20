{
    "server": "YouTube Utilities",
    "transport": "http",
    "port": 8083,
    "settings": [
        # add 3 mcp tools
        {
            "agentmake": {"tool": "youtube/transcribe_google"},
        },
        {
            "agentmake": {"tool": "youtube/download_video"},
        },
        {
            "agentmake": {"tool": "youtube/download_audio"},
        },
        # add a mcp prompt
        {
            "name": "youtube_all",
            "description": "Transcribe a Youtube video and download it into both video and audio files",
            "agentmake": """You are a Youtube agent. Your goal is to transcribe a Youtube video and download it into both video and audio files, when you are given a YouTube URL.
    
Please perform the following steps in order:
1. Call the tool `youtube_transcribe_google` to transcribe a YouTube video.
2. Call the tool `youtube_download_video` to download it into a video file.
3. Call the tool `youtube_download_audio` to download it into an audio file.
4. Give me the transcription and the paths to both downloaded files.
"""
        },
    ]
}