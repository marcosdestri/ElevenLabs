"""LLM step — injectable client for deterministic tests."""

from __future__ import annotations

from unittest.mock import MagicMock

from voice_agent.llm import generate_response


def test_generate_response_uses_injected_client() -> None:
    mock_completion = MagicMock()
    mock_completion.choices = [
        MagicMock(message=MagicMock(content="  Hello from mock.  "))
    ]
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_completion

    text = generate_response("Hi there", client=mock_client)

    assert text == "Hello from mock."
    mock_client.chat.completions.create.assert_called_once()
    messages = mock_client.chat.completions.create.call_args.kwargs["messages"]
    assert messages[-1]["role"] == "user"
    assert messages[-1]["content"] == "Hi there"
