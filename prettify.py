#!/usr/bin/env python3

"""
Website: https://pythonadventures.wordpress.com/2011/04/03/prettify-html-with-beautifulsoup/
Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

Prettify an HTML page. The script prints the HTML source
that is built by BeautifulSoup (BS).
Idea: if you want to manipulate a page with BS, analyze
      the prettified source because this is how BS
      stores it.

Usage: prettify <URL>

Last update: 2017-01-08 (yyyy-mm-dd)
"""

import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}


def process(url):
    r = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(r.text, "lxml")

    return soup.prettify()


def main():
    if len(sys.argv) == 1:
        print("Usage: {0} <URL>".format(Path(sys.argv[0]).name))
        sys.exit(1)
    # else, if at least one parameter was passed
    print(process(sys.argv[1]))

#############################################################################

if __name__ == "__main__":
    main()
