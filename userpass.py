#!/usr/bin/env python3

"""
Username and password generator.

Made for online registrations.
"""

import string
from random import choice

from lib import utils
from lib import markov_passwords
from lib.markov_usernames import MName
from lib.tabulate import tabulate

#############################################################################

def get_username_1():
    """
    Returns a Western-style username.
    """
    return MName().New()

def get_username_2(length=6):
    """
    Returns a readable (Japanese-style) username.
    """
    return markov_passwords.get_word(length)

#############################################################################

def get_password_1(length=8):
    """
    Create a password with uppercase letters, lowercase letters, and digits.

    The password will include lowercase letters with higher probability.
    """
    assert length >= 8
    #
    chars = string.ascii_lowercase + string.ascii_lowercase + string.ascii_lowercase + \
            string.ascii_uppercase + string.digits + string.digits + string.digits
    chars = ''.join(utils.my_shuffle([x for x in chars]))
    return ''.join(choice(chars) for x in range(length))


def get_password_2(length=8):
    """
    Get data from /dev/urandom .
    """
    assert length >= 8
    #
    li = []
    with open("/dev/urandom", "rb") as f:
        while len(li) < length:
            c = f.read(1)
            if c.isalnum():
                li.append(c.decode("ascii"))

    return ''.join(li)

#############################################################################

if __name__ == "__main__":
    table = []
    headers = ["Username #1", "Username #2", "Password #1", "Password #2"]
    for _ in range(10):
        name1 = get_username_1()
        name2 = get_username_2()
        pass1 = get_password_1(8)
        pass2 = get_password_2(12)
        table.append([name1, name2, pass1, pass2])
#        print("{:15}{:15}{:15}{:15}".format(name1, name2, pass1, pass2))
    print(tabulate(table, headers=headers, tablefmt="psql"))
