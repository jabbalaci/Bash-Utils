#!/usr/bin/env python3

"""
A simple script that changes the character
encoding of the input file to UTF-8.

The result is printed to the screen.

Last update: 2017-12-16 (yyyy-mm-dd)
"""

import os
import sys
from pathlib import Path

import config as cfg
from lib import fs
from lib.process import get_simple_cmd_output

fs.check_if_available(cfg.FILE, "Error: {} is not available!".format(cfg.FILE))
fs.check_if_available(cfg.ICONV, "Error: {} is not available!".format(cfg.ICONV))

force_conversion = False


def print_help():
    p = Path(sys.argv[0])
    print("""
Usage: {0} input.txt [-f] [-h|--help]

-f              force conversion (even if the input is in UTF-8)
-h, --help      this help
""".strip().format(p.name))


def process(fname):
    cmd = 'file -i "{}"'.format(fname)
    res = get_simple_cmd_output(cmd).strip()
    charset = None
    if 'charset=' in res:
        charset = res.split('charset=')[1].lower()
    if not charset:
        print("Error: cannot determine the character encoding of the input file.", file=sys.stderr)
        exit(2)
    if charset == 'utf-8':
        if not force_conversion:
            print("Warning: the input file is already in UTF-8 encoding.", file=sys.stderr)
            print("Tip: use the -f option to force conversion.", file=sys.stderr)
            return
    # else
    cmd = 'iconv --from-code={src} --to-code=utf-8 "{f}"'.format(src=charset, f=fname)
    os.system(cmd)


def main():
    global force_conversion
    
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()
        exit(1)
    # else
    if '-f' in sys.argv:
        force_conversion = True
        sys.argv.remove('-f')
    if len(sys.argv) == 1:
        print_help()
        exit(1)
    # else
    process(sys.argv[1])

##############################################################################

if __name__ == "__main__":
    main()
