"""Configuration edge cases."""

from __future__ import annotations

import pytest

from voice_agent.settings import require_env


def test_require_env_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("VOICE_AGENT_TEST_KEY", raising=False)
    with pytest.raises(RuntimeError, match="VOICE_AGENT_TEST_KEY"):
        require_env("VOICE_AGENT_TEST_KEY", "Set it in .env for local runs.")
