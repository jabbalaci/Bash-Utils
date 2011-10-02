#!/usr/bin/env python

"""
A very simple lookup of a word.
"""

import sys
import webbrowser


_template = 'http://www.thefreedictionary.com/p/{word}'


def process(word):
    url = _template.format(word=word)
    webbrowser.open(url)
    print '# see the result in your web browser'
    
    
#############################################################################


if __name__ == "__main__":
    if len(sys.argv) > 1:
        process(sys.argv[1])
    else:
        print >>sys.stderr, "{0}: error: specify a word.".format(sys.argv[0])
        sys.exit(1)
