#!/usr/bin/env python3
# encoding: utf-8

"""
Working with webpages.

# from jplib import web
# from jplib.web import get_page
"""

import sys

import requests

import config as cfg
from lib.timeout import Timeout

headers = {
    'User-Agent': cfg.USER_AGENT,
}

MAX = 999


def get_page(url, debug=False, user_agent=True, timeout=MAX):
    try:
        with Timeout(timeout):
            if user_agent:
                r = requests.get(url, headers=headers, timeout=timeout)
            else:
                r = requests.get(url, timeout=timeout)
            #
            return r.text
    except Timeout.Timeout:
        if debug:
            print("# timeout error", file=sys.stderr)
        return None
    except requests.exceptions.ConnectionError as e:
        if debug:
            print("#", e, file=sys.stderr)
        return None

##############################################################################

if __name__ == "__main__":
    url = "http://hup.hu"
#    print(get_js_page(url))
    print(get_js_page(url, 1))
