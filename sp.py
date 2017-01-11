#!/usr/bin/env python3

"""
Website: https://ubuntuincident.wordpress.com/2011/03/17/show-the-absolute-path-of-a-file/
Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

Print the absolute path of a file (sp.py means "show path").
If no parameter is passed, show the current path.
The output is also copied to the clipboards.

Usage: sp <filename> [-n]

The option "-n" means normal output, i.e. spaces are not protected with
a backslash.

Last update: 2017-01-09 (yyyy-mm-dd)
"""

import os
import sys

import config as cfg
from lib import fs
from lib.clipboard import text_to_clipboards

fs.check_if_available(cfg.XSEL, "Error: {} is not available!".format(cfg.XSEL))


def main():
    normal = False
    if "-n" in sys.argv:
        normal = True
        sys.argv.remove("-n")

    if len(sys.argv) == 1:
        text = os.getcwd()
    else:
        text = os.path.join(os.getcwd(), sys.argv[1])

    if not normal:
        text = text.replace(' ', r'\ ')
    print('# copied to the clipboard', file=sys.stderr)
    print(text)
    text_to_clipboards(text)

##############################################################################

if __name__ == '__main__':
    main()
