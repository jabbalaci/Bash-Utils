#!/usr/bin/env python3

"""
Rename a file/directory interactively.

It needs just one command-line argument: the name of a file/directory
that you want to rename.
"""

import os
import readline
import shutil
import sys


def rlinput(prompt, prefill=""):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("# error: provide just one argument!")
        sys.exit(1)
    # else
    fname = args[0]
    try:
        new_name = rlinput("New name: ", prefill=fname)
    except KeyboardInterrupt:
        print()
        print("# interrupted")
        return
    # if there was no exception
    if fname == new_name:
        print("# warning: you didn't change anything")
        return
    # else
    if os.path.exists(new_name):
        print(f"# error: the file/directory '{new_name}' already exists!")
        sys.exit(2)
    # else
    shutil.move(fname, new_name)
    if os.path.exists(new_name):
        print(f"# '{fname}' -> '{new_name}'")
    else:
        print("# something went wrong")


##############################################################################

if __name__ == "__main__":
    main()
