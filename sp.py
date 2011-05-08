#!/usr/bin/env python

# Website: https://ubuntuincident.wordpress.com/2011/03/17/show-the-absolute-path-of-a-file/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
#
# Print the absolute path of a file.
# If no parameter is passed, show the current path.
# sp.py -> "show path"
#
# Usage: sp <filename>

import os.path
import sys

if len(sys.argv) == 1:
    print os.getcwd()
else:
    print os.path.join(os.getcwd(), sys.argv[1])
