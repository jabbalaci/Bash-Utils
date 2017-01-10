#!/usr/bin/env python3

"""
a simple scraper for http://sloganmaker.com/sloganmaker.php
"""

import sys
from urllib.parse import urlencode

import requests

from lib.scraper import bsoup as bs


BASE = 'http://sloganmaker.com/sloganmaker.php?'


def get_slogan(word, times=1):
    assert 1 <= times <= 10     # be nice with the server
    #
    li = []
    url = BASE + urlencode({'user': word})
    for _ in range(times):
        text = requests.get(url).text
        soup = bs.to_soup(text)
#        import ipdb; ipdb.set_trace()
        slogan = soup.select('body div p')[0].text
        if slogan.count('.') == 1 and not slogan[0].isupper():
            slogan = slogan.replace('.', '')
        if len(slogan) >= 2 and slogan[-1] == '.' and slogan[-2] == '!':
            slogan = slogan[:-1]
        li.append(slogan)

    return li

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Error: specify a keyword.', file=sys.stderr)
        sys.exit(1)
    # else
    word = sys.argv[1]
    times = 5
    try:
        times = int(sys.argv[2])
    except:
        pass
    for s in get_slogan(word, times):
        print(s)
