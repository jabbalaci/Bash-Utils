#!/usr/bin/env python3

"""
"platform" is in the standard library, so it was renamed to podium :)
"""

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import getpass
import platform as p
import socket
import uuid

from lib.jhash import string_to_md5


def get_hostname():
    """
    echo $HOSTNAME
    """
    return socket.gethostname()


def get_home_dir():
    """
    echo $HOME
    """
    return os.path.expanduser('~')


def get_username():
    """
    echo $USER
    """
    return getpass.getuser()


def is_linux():
    """
    Is the current platform Linux?
    """
    return sys.platform.startswith('linux')


def get_distro():
    """
    Name of your Linux distro (in lowercase).
    """
    with open("/etc/issue") as f:
        return f.read().lower().split()[0]


def get_fingerprint(md5=False):
    """
    Fingerprint of the current operating system/platform.

    If md5 is True, a digital fingerprint is returned.
    """
    sb = []
    sb.append(p.node())
    sb.append(p.architecture()[0])
    sb.append(p.architecture()[1])
    sb.append(p.machine())
    sb.append(p.processor())
    sb.append(p.system())
    sb.append(str(uuid.getnode()))    # MAC address
    text = '#'.join(sb)
    if md5:
        return string_to_md5(text)
    else:
        return text


def get_short_fingerprint(length=6):
    """
    A short digital fingerprint of the current operating system/platform.

    Length should be at least 6 characters.
    """
    assert 6 <= length <= 32
    #
    return get_fingerprint(md5=True)[-length:]

#############################################################################

if __name__ == "__main__":
    print(get_hostname())
    print(get_home_dir())
    print(get_username())
    print(is_linux())
    print(get_fingerprint())
    print(get_fingerprint(True))
    print(get_distro())
    print("Short fingerprint:", get_short_fingerprint())
