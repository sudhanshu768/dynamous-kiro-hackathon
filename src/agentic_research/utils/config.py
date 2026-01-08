"""
Minimal configuration for Agentic Research Engineer (Phase 4).
"""

import os


class Config:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.default_ai_provider = os.getenv("DEFAULT_AI_PROVIDER", "openai")

        # Phase 4 flag
        self.enable_ai = os.getenv("ENABLE_AI", "false").lower() == "true"


config = Config()

