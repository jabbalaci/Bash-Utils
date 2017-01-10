#!/usr/bin/env python3

"""
Network-related stuff.

# from jplib import network
"""

import json
import re
import socket

from lib import process
from lib.process import get_return_code_of_simple_cmd
from lib.web import get_page
from six.moves.urllib import error, request

URL = 'http://www.google.com'


def is_internet_on(method=1, debug=False):
    """Check if the Internet connection is on."""

    if method == 1:
        # At my current place we have a wifi that redirects to a login page,
        # so we always have a connection. That's why I check the content of
        # the fetched webpage.
        text = get_page(URL, timeout=3, debug=debug)
        if text:
            if '<title>Google</title>' in text:
                return True
        # else:
        return False
    elif method == 2:
        # http://stackoverflow.com/questions/3764291/checking-network-connection
        try:
            request.urlopen('http://www.google.com', timeout=3)
            return True
        except error.URLError:
            return False
        except socket.timeout:
            return False
    elif method == 3:
        cmd = "ping -c 1 www.google.com"
        return get_return_code_of_simple_cmd(cmd) == 0
    else:
        print('# warning: unknown method in is_internet_on()')


def get_my_external_ip():
    """
    Get my external IP.

    Local IP: http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    """
    content = get_page("http://jsonip.com/")
    if content:
        d = json.loads(content)
        return d["ip"]
    else:
        return None


def ping(host, cnt=1):
    """Ping a URL and return the average ping time."""
    cmd = 'ping -c {cnt} {url}'.format(url=host, cnt=cnt)
    output = [x for x in process.get_simple_cmd_output(cmd).split('\n') if x]
    result = re.search('min/avg/max/mdev = (.*)/(.*)/(.*)/(.*) ms', output[-1])
    if result:
        return float('{0:.2f}'.format(float(result.group(1))))
    else:
        return None


def fping(host, cnt=1):
    """
    Get the avg ping time of a host (in msec).

    Instead of ping we use the command fping.
    """
    host = host.split(':')[0]
    cmd = "fping {host} -C {cnt} -q".format(host=host, cnt=cnt)
    res = [float(x) for x in process.get_simple_cmd_output(cmd).strip().split(':')[-1].split() if x != '-']
    if len(res) > 0:
        return sum(res) / len(res)
    else:
        return None

#############################################################################

if __name__ == "__main__":
    print(is_internet_on())
    print(get_my_external_ip())
    #
    host = 'www.google.com'
    print(ping(host, 2))
    print(fping(host, 2))
