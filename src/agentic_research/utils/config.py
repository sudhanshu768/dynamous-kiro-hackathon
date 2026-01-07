"""
Minimal configuration for Agentic Research Engineer (Phase 1).
No AI logic. No validation. Just environment access.
"""

import os


class Config:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.default_ai_provider = os.getenv("DEFAULT_AI_PROVIDER", "openai")


config = Config()

