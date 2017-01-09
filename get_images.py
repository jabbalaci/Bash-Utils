#!/usr/bin/env python3

"""
Extract image links from a web page
===================================
Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
GitHub:  https://github.com/jabbalaci/Bash-Utils

Given a webpage, extract all image links.

Usage:
------
get_images.py URL [URL]... [options]

Options:
  -l, --length  Show lengths of images.

Last update: 2017-01-09 (yyyy-mm-dd)
"""

import sys
import urllib
from optparse import OptionParser
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}


def get_content_length(url):
    try:
        h = requests.get(url, headers=user_agent).headers
        return h['content-length']
    except:
        return "?"


def process(url, options):
    r = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(r.text, "lxml")

    for tag in soup.findAll('img', src=True):
        image_url = urljoin(url, tag['src'])
        print(image_url, end='')
        if options.length:
            length = get_content_length(image_url)
            print('', length, end='')
        print()


def main():
    parser = OptionParser(usage='%prog URL [URL]... [options]')

    #[options]
    parser.add_option('-l',
                      '--length',
                      action='store_true',
                      default=False,
                      help='show lengths of images')

    options, arguments = parser.parse_args()

    if not arguments:
        parser.print_help()
        sys.exit(1)
    # else, if at least one parameter was passed
    for url in arguments:
        process(url, options)

#############################################################################

if __name__ == "__main__":
    main()
