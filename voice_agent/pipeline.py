"""Orchestrates one customer turn: input → response → voice."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from voice_agent import settings
from voice_agent.llm import generate_response
from voice_agent.tts import generate_voice


def read_customer_input(prompt: str = "User: ") -> str:
    """Step 1 — User input: capture the customer's message.

    CLI typing stands in for speech-to-text; swap this boundary only when
    adding STT—downstream steps stay the same.
    """
    return input(prompt).strip()


def run_single_turn(
    *,
    read_input: Callable[[], str] | None = None,
    output_path: Path | None = None,
) -> None:
    """Execute the three-stage pipeline once: User Input → Response → Voice."""
    settings.load_local_env()

    # --- Stage 1: User input ---
    get_line = read_input or (lambda: read_customer_input())
    customer_utterance = get_line()
    if not customer_utterance:
        raise RuntimeError("Empty input; type a message after User: and press Enter.")

    # --- Stage 2: Response generation (LLM; see llm.py) ---
    assistant_reply = generate_response(customer_utterance)
    print("AI:", assistant_reply)

    # --- Stage 3: Voice output (TTS; see tts.py) ---
    audio_path = generate_voice(assistant_reply, output_path)
    print(f"Saved audio to {audio_path.resolve()}")
