"""Orchestration: input → response → voice (single customer turn)."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from voice_agent import settings
from voice_agent.llm import generate_response
from voice_agent.tts import synthesize_voice_file


def run_single_turn(
    *,
    read_input: Callable[[], str] | None = None,
    output_path: Path | None = None,
) -> None:
    """Execute one full turn. ``read_input`` defaults to terminal ``input``."""
    settings.load_local_env()

    get_line = read_input or (lambda: input("User: ").strip())

    # --- input ---
    user_message = get_line()
    if not user_message:
        raise RuntimeError("Empty input; type a message after User: and press Enter.")

    # --- response ---
    reply = generate_response(user_message)
    print("AI:", reply)

    # --- voice ---
    out = synthesize_voice_file(reply, output_path)
    print(f"Saved audio to {out.resolve()}")
