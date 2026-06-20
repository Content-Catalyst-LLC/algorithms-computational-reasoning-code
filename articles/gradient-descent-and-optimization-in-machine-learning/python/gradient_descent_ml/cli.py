# CLI for gradient descent and machine learning optimization workflows.

from __future__ import annotations

try:
    from .audit import main
except ImportError:  # Allows direct execution as a script.
    from pathlib import Path
    import sys

    sys.path.append(str(Path(__file__).resolve().parent))
    from audit import main  # type: ignore


if __name__ == "__main__":
    main()
