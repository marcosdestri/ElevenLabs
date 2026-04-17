"""CLI entrypoint."""

from __future__ import annotations

import sys

from voice_agent.pipeline import run_single_turn


def main() -> None:
    try:
        run_single_turn()
    except RuntimeError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
    except OSError as err:
        print(f"Failed to write audio file: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
