#!/usr/bin/env python3

"""
Extract all links from a web page
=================================
Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://pythonadventures.wordpress.com/2011/03/10/extract-all-links-from-a-web-page/
GitHub:  https://github.com/jabbalaci/Bash-Utils

Given a webpage, extract all links.

Usage:
------
./get_links.py <URL>

Last update: 2017-01-08 (yyyy-mm-dd)
"""

import sys
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}


def process(url):
    r = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(r.text, "lxml")

    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(url, tag['href'])
        print(tag['href'])


def main():
    if len(sys.argv) == 1:
        print("Usage: {0} URL [URL]...".format(Path(sys.argv[0]).name))
        sys.exit(1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
        process(url)

#############################################################################

if __name__ == "__main__":
    main()
