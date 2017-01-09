#!/usr/bin/env python3

"""
print the content of the clipboard to the standard output

Last update: 2017-01-08 (yyyy-mm-dd)
"""

import sys

from lib import clipboard as cb


def print_help():
    print("""
Usage: {0} [options]

Options:
    -h, --help        this help
    -1                read from primary clipboard (default)
    -2                read from secondary clipboard
""".strip().format(sys.argv[0]))


def process_parameters(params):
    for e in params:
        if e == "-1":
            print(cb.read_primary())
        elif e == "-2":
            print(cb.read_clipboard())
        else:
            print("Error: {0} is an unknown option.".format(e))
            exit(1)

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("-1")    # default
    # else
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()
        exit(0)
    # else
    process_parameters(sys.argv[1:])
