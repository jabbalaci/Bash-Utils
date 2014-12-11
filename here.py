#!/usr/bin/env python2
# encoding: utf-8

"""
Laszlo Szathmary, 2014 (jabba.laci@gmail.com)

Print just the name of the current directory.
For instance, if you are in "/home/students/solo",
then this script will print just "solo".

The output is also copied to the clipboard.

Usage: here
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
import sys
from tocb import text_to_clipboards


def main():
    text = os.path.split(os.getcwd())[1]
    print('# copied to the clipboard', file=sys.stderr)
    print(text)
    text_to_clipboards(text)

##############################################################################

if __name__ == "__main__":
    main()
