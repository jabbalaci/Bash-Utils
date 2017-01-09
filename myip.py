#!/usr/bin/env python3

"""
My external IP address.
"""

import requests


def get_my_external_ip():
    try:
        d = requests.get("http://jsonip.com/").json()
        return d["ip"]
    except:
        return None

#############################################################################

if __name__ == "__main__":
    print(get_my_external_ip())
