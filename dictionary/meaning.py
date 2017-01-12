#!/usr/bin/env python3

"""
A very simple lookup of a word.

Last update: 2017-01-08 (yyyy-mm-dd)
"""

import sys
import webbrowser
from pathlib import Path

template = 'http://www.thefreedictionary.com/{word}'


def process(word):
    url = template.format(word=word)
    webbrowser.open(url)
    print('# see the result in your web browser')


#############################################################################


if __name__ == "__main__":
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print("{0}: specify a word".format(Path(sys.argv[0]).name), file=sys.stderr)
        sys.exit(1)
