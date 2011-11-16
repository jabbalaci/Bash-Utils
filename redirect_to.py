#!/usr/bin/env python

"""
Where does a URL redirect?
==========================

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: http://pythonadventures.wordpress.com/2010/12/21/where-does-a-page-redirect-to/
GitHub:  https://github.com/jabbalaci/Bash-Utils

This script tells you where a webpage redirects.

Example:
--------

$ ./redirect_to.py http://bottlepy.org      # calling the script
http://bottlepy.org/docs/dev/               # output
"""

import sys
import urllib


def redirect(url):
    try:
        page = urllib.urlopen(url)
        return page.geturl()
    except:
        print 'Error: there is something wrong with that URL'
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage: {0} <url>".format(sys.argv[0])
    else:
        print redirect(sys.argv[1])
