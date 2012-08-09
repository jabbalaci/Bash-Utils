#!/usr/bin/env python

# Website: https://pythonadventures.wordpress.com/2011/04/03/prettify-html-with-beautifulsoup/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
#
# Prettify an HTML page. The script prints the HTML source
# that is built by BeautifulSoup (BS).
# Idea: if you want to manipulate a page with BS, analyze
#       the prettified source because this is how BS
#       stores it.
#
# Usage: prettify <URL>

import sys
import urllib
from BeautifulSoup import BeautifulSoup


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


def process(url):
    myopener = MyOpener()
    #page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)
    return soup.prettify()
# process(url)


def main():
    if len(sys.argv) == 1:
        print "Jabba's HTML Prettifier v0.1"
        print "Usage: %s <URL>" % sys.argv[0]
        sys.exit(-1)
    # else, if at least one parameter was passed
    print process(sys.argv[1])
# main()

if __name__ == "__main__":
    main()
