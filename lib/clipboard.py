#!/usr/bin/env python2

"""
Copy text to clipboards (to both of them).
This solution here is specific to Linux.

For a platform independent solution, you can check out
https://github.com/asweigart/mapitpy/blob/master/pyperclip.py
(I didn't try it).

# from jpl2.clipboard import text_to_clipboards
# from jpl2 import clipboard
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import subprocess

from lib import process


def text_to_clipboards(text):
    """Copy text to both clipboards."""
    to_primary(text)
    to_clipboard(text)

#############################################################################

def to_primary(text):
    """Write text to 'primary'."""
    xsel_proc = subprocess.Popen(['xsel', '-pi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text.encode())


def to_clipboard(text):
    """Write text to 'clipboard'."""
    xsel_proc = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text.encode())

#############################################################################

def read_primary():
    """Read content of 'primary'."""
    cmd = 'xsel -po'
    return process.get_simple_cmd_output(cmd)


def read_clipboard():
    """Read content of 'clipboard'."""
    cmd = 'xsel -bo'
    return process.get_simple_cmd_output(cmd)

#############################################################################

def clear_both_clipboards():
    """Clear both clipboards."""
    clear_primary()
    clear_clipboard()


def clear_primary():
    """Clear primary."""
    process.execute_cmd('xsel -pc')


def clear_clipboard():
    """Clear clipboard."""
    process.execute_cmd('xsel -bc')

#############################################################################

if __name__ == "__main__":
    text = "this should go on the clipboards"
    print(text)
    text_to_clipboards(text)
    #
    print('primary>', read_primary())
    print('clipboard>', read_clipboard())
