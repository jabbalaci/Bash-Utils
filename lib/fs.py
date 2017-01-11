import sys
from pathlib import Path


def check_if_available(prg, msg):
    """
    Check if the given program is available.
    If not, then die with the given error message.
    """
    if not Path(prg).is_file():
        print(msg, file=sys.stderr)
        sys.exit(1)
