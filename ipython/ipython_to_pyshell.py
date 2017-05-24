#!/usr/bin/env python3

"""
Convert an IPython history file to the format of a
normal Python shell.

Why? You want to paste a Python shell snippet to your
blog post but you want to write it in IPython (as it's
more comfortable to use).

How to export the IPython history?

    %history -op -f ipy_history.txt
"""

import sys


def convert(s):
    if s.startswith(">>> %"):
        return None
    # else
    return s
        

def process(fname):
    f = open(fname)
    for line in f:
        line = line.rstrip('\n')
        res = convert(line)
        if res:
            print(res)
    f.close()

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ipython_to_pyshell ipy_history.txt", file=sys.stderr)
        exit(1)
    # else
    fname = sys.argv[1]
    process(fname)
