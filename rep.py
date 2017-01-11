#!/usr/bin/env python3

"""
Repat a bash command several times.

Usage:

    rep 5 echo hello

It will print "hello" five times.
"""

import os
import sys
from pathlib import Path


class MissingCommandException(Exception):
    pass


def print_usage():
    print("""
Usage: {} [rep] [cmd]
Where:
  rep    is the repetition (e.g. 5)
  cmd    is the command to run (e.g. echo hello)
""".strip().format(Path(sys.argv[0]).name))


def run(rep, cmd):
    for i in range(1, rep+1):
        # print(cmd)
        os.system(cmd)

##############################################################################

if __name__ == "__main__":
    try:
        rep = int(sys.argv[1])
        cmd = " ".join(sys.argv[2:])
        if not cmd:
            raise MissingCommandException
    except (IndexError, ValueError, MissingCommandException):
        print_usage()
        sys.exit(1)
    # else
    run(rep, cmd)
