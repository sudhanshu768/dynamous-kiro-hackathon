"""
Configuration for Agentic Research Engineer (Phase 7B).
"""

import os


class Config:
    def __init__(self):
        self.enable_ai = os.getenv("ENABLE_AI", "false").lower() == "true"
        self.ai_provider = os.getenv("AI_PROVIDER", "openai")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")


config = Config()

