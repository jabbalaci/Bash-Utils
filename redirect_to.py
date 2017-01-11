#!/usr/bin/env python3

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

Last update: 2017-01-09 (yyyy-mm-dd)
"""

import sys
from pathlib import Path

import requests


def redirect(url):
    try:
        r = requests.get(url)
        return r.url
    except:
        print('Error: there is something wrong with that URL')
        sys.exit(1)

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: {0} <url>".format(Path(sys.argv[0]).name))
    else:
        print(redirect(sys.argv[1]))
