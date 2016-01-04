#!/usr/bin/env python3

# Website: https://pythonadventures.wordpress.com/2011/03/05/copy-string-to-x-clipboards/
# Laszlo Szathmary, 2011--2012 (jabba.laci@gmail.com)
#
# Copy the text from the standard input to ALL clipboards. Thus, you can use
# any paste method to insert your text (middle mouse button or Shift+Insert).
# tocb.py -> "to clipboard(s)"
#
# Requirement: xsel package (sudo apt-get install xsel).
#
# Usage: cat file.txt | tocb

import sys
import subprocess

#############################################################################


def text_to_clipboards(text):
    text = str.encode(text)
    # "primary":
    xsel_proc = subprocess.Popen(['xsel', '-pi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)
    # "clipboard":
    xsel_proc = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)

#############################################################################

if __name__ == "__main__":
    stuff = sys.stdin.read()
    text_to_clipboards(stuff)
