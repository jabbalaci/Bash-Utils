#!/usr/bin/env python

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
"""

import sys
import urllib
import urlparse

from optparse import OptionParser
from BeautifulSoup import BeautifulSoup


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
# MyOpener


def get_url_info(url):
    d = urllib.urlopen(url)
    return d.info()
# get_url_info


def process(url, options):
    myopener = MyOpener()
    #page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    for tag in soup.findAll('img', src=True):
        image_url = urlparse.urljoin(url, tag['src'])
        image_info = get_url_info(image_url)
        print image_url,
        if options.length:
            print image_info['Content-Length'],
        print
# process


def main():
    parser = OptionParser(usage='%prog URL [URL]... [options]')

    #[options]
    parser.add_option('-l',
                      '--length',
                      action='store_true',
                      default=False,
                      help='Show lengths of images.')

    options, arguments = parser.parse_args()

    if not arguments:
        parser.print_help()
        sys.exit(1)
    # else, if at least one parameter was passed
    for url in arguments:
        process(url, options)
# main

#############################################################################

if __name__ == "__main__":
    main()
