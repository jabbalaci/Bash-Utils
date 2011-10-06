#!/usr/bin/env python

# Change spaces to underscores.
# When to use: creating directories/files and we want to avoid spaces
#              in their names.
#
# Example:
# --------
# mv thinkpython.pdf `us "How to Think Like a Computer Scientist.pdf"`
#     => How_to_Think_Like_a_Computer_Scientist.pdf
#
# Usage: us <text>

import sys


def main(argv):
    if len(argv) > 1:
        text = argv[1]
        print text.replace(' ', '_')

if __name__ == "__main__":
    main(sys.argv)
