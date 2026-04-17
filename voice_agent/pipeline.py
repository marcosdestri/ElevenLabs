"""Orchestrates one customer turn: input → response → voice."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from voice_agent import settings
from voice_agent.llm import generate_response
from voice_agent.tts import generate_voice


def read_customer_input(prompt: str = "User: ") -> str:
    """Step 1 — Input: read what the customer said.

    Today this is typed text in the CLI. The same function boundary is where
    speech-to-text would plug in for a true voice-in experience.
    """
    return input(prompt).strip()


def run_single_turn(
    *,
    read_input: Callable[[], str] | None = None,
    output_path: Path | None = None,
) -> None:
    """Run one full turn: capture input, generate text reply, generate voice file."""
    settings.load_local_env()

    # Step 1 — Input
    get_line = read_input or (lambda: read_customer_input())
    user_message = get_line()
    if not user_message:
        raise RuntimeError("Empty input; type a message after User: and press Enter.")

    # Step 2 — Response (LLM)
    assistant_text = generate_response(user_message)
    print("AI:", assistant_text)

    # Step 3 — Voice (TTS)
    audio_path = generate_voice(assistant_text, output_path)
    print(f"Saved audio to {audio_path.resolve()}")
