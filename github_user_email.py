#!/usr/bin/env python3
# encoding: utf-8

"""
Figure out the email of a github user.

Steps from here: http://www.eremedia.com/sourcecon/how-to-find-almost-any-github-users-email-address/
Protection tips: https://help.github.com/articles/keeping-your-email-address-private/

Author:

Laszlo Szathmary, alias Jabba Laci, 2016
jabba.laci@gmail.com
"""

import re
import sys

import requests

URL = "https://api.github.com/users/{name}/events/public"


def get_input():
    try:
        inp = input("Github info (username or repo. link): ").strip()
        if inp:
            if '/' not in inp:
                return inp
            # else:
            m = re.search(r'github.com/([^/]+)', inp)
            if m:
                return m.group(1)
            else:
                print('Invalid input.')
        else:
            print('Invalid input.')
    except (KeyboardInterrupt, EOFError):
        print()
        print('aborted.')
        sys.exit(1)


def extract_email(name):
    url = URL.format(name=name)
    li = requests.get(url).json()
    try:
        for d in li:
            if d['type'] == 'PushEvent':
                return d['payload']['commits'][0]['author']['email']
    except TypeError:
        return None

    return None


def main():
    username = get_input()
    email = extract_email(username)
    if email:
        print(email)
    else:
        print("Error: the email couldn't be extracted.")

##############################################################################

if __name__ == "__main__":
    main()
