"""Backward-compatible entrypoint — delegates to ``voice_agent.cli``."""

from voice_agent.cli import main

if __name__ == "__main__":
    main()
