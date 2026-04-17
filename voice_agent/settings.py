"""Configuration: paths, API defaults, and environment loading."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent
DOTENV_PATH = PROJECT_ROOT / ".env"

# ElevenLabs REST
ELEVENLABS_TTS_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
# Customer-heard artifact (not a generic "output.bin")
DEFAULT_OUTPUT = PROJECT_ROOT / "voice_response.mp3"
REQUEST_TIMEOUT_S = 60

# OpenAI Chat Completions
DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = (
    "You are a helpful voice assistant. Reply in clear, natural language suitable "
    "to be read aloud. Keep answers concise unless the user asks for detail."
)


def load_local_env() -> None:
    """Load `.env` from project root so runs do not depend on shell cwd."""
    load_dotenv(DOTENV_PATH)


def require_env(name: str, setup_hint: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is missing or empty. {setup_hint}")
    return value


def openai_api_key() -> str:
    return require_env(
        "OPENAI_API_KEY",
        "Add it to `.env` as OPENAI_API_KEY=sk-... (no spaces around `=`) or export it.",
    )


def elevenlabs_api_key() -> str:
    return require_env(
        "ELEVENLABS_API_KEY",
        "Add it to `.env` as ELEVENLABS_API_KEY=... (no spaces around `=`) or export it.",
    )


def openai_model() -> str:
    return (os.environ.get("OPENAI_MODEL") or DEFAULT_OPENAI_MODEL).strip()
