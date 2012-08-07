#!/usr/bin/env python

# Website: https://ubuntuincident.wordpress.com/2011/03/17/show-the-absolute-path-of-a-file/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
#
# NEW! The path is also copied to the clipboard.
#
# Print the absolute path of a file.
# If no parameter is passed, show the current path.
# sp.py -> "show path"
#
# Usage: sp <filename>

import os
import sys
from tocb import text_to_clipboards


if len(sys.argv) == 1:
    text = os.getcwd()
else:
    text = os.path.join(os.getcwd(), sys.argv[1])

print '# copied to the clipboard'
print text
text_to_clipboards(text)
