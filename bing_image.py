#!/usr/bin/env python3

"""
Bing Image
==========

Extract the URL of the background image on `bing.com`.

Author:  Laszlo Szathmary, 2021 (jabba.laci@gmail.com)
GitHub:  https://github.com/jabbalaci/Bash-Utils

Last update: 2021-08-05 (yyyy-mm-dd)
"""

import re
import urllib.request

URL = "https://www.bing.com"


def get_page(url):
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")


def main():
    html = get_page(URL)
    m = re.search(r'<link rel="preload" href="(.*?)" as="image" id="preloadBg"', html)
    if m:
        url = m.group(1)
        url = url.split("&amp;")[0]
        url = URL + url
        print(url)

##############################################################################

if __name__ == "__main__":
    main()
