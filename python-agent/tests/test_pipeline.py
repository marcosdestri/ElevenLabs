"""End-to-end turn orchestration (mocked external APIs)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from voice_agent.pipeline import run_single_turn


def test_run_single_turn_order_and_io(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("ELEVENLABS_API_KEY", "test-eleven-key")

    out_mp3 = tmp_path / "test_out.mp3"
    out_mp3.write_bytes(b"")

    with patch(
        "voice_agent.pipeline.generate_response",
        return_value="Assistant reply.",
    ) as mock_llm, patch(
        "voice_agent.pipeline.generate_voice",
        return_value=out_mp3,
    ) as mock_tts:
        run_single_turn(
            read_input=lambda: "Customer question?",
            output_path=out_mp3,
        )

    mock_llm.assert_called_once_with("Customer question?")
    mock_tts.assert_called_once_with("Assistant reply.", out_mp3)


def test_run_single_turn_rejects_empty_input(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    monkeypatch.setenv("ELEVENLABS_API_KEY", "y")

    with pytest.raises(RuntimeError, match="Empty input"):
        run_single_turn(read_input=lambda: "")
