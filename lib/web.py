#!/usr/bin/env python3
# encoding: utf-8

"""
Working with webpages.

# from jplib import web
# from jplib.web import get_page
"""

import sys

import requests
from unipath import Path

from jplib import config as cfg
from jplib import fs
from jplib.process import get_simple_cmd_output
from jplib.timeout import Timeout

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


def get_js_page(url, wait=None):
    """Get a page with Webkit, i.e. evaluate embedded JavaScripts."""
    prg = Path(cfg.ROOT_DIR, "scraper", "jabba_webkit.py")
    cmd = 'python2 {prg} "{url}" {wait}'.format(
        prg=prg,
        url=url,
        wait=wait if wait else ""
    )
    return get_simple_cmd_output(cmd)
    # return get_exitcode_stdout_stderr(cmd)[1]


def download_to(url, local_file, user_agent=True, timeout=MAX, overwrite=False, encode="utf8"):
    """Fetch the content of a URL and store it in a local file."""
    content = get_page(url, user_agent=user_agent, timeout=timeout)
    fs.store_content_in_file(content, local_file, overwrite=overwrite, encode=encode)

##############################################################################

if __name__ == "__main__":
    url = "http://hup.hu"
#    print(get_js_page(url))
    print(get_js_page(url, 1))
