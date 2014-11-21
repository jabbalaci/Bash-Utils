#!/usr/bin/env python
# encoding: utf-8

"""
Website: https://ubuntuincident.wordpress.com/2011/03/17/show-the-absolute-path-of-a-file/
Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

Print the absolute path of a file (sp.py means "show path").
If no parameter is passed, show the current path.
The output is also copied to the clipboards.

Usage: sp <filename>
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
import sys
from tocb import text_to_clipboards


def main():
    if len(sys.argv) == 1:
        text = os.getcwd()
    else:
        text = os.path.join(os.getcwd(), sys.argv[1])

    text = text.replace(' ', r'\ ')
    print('# copied to the clipboard', file=sys.stderr)
    print(text)
    text_to_clipboards(text)

##############################################################################

if __name__ == '__main__':
    main()
