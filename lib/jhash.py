#!/usr/bin/env python3

"""
hashlib

# from lib.jhash import string_to_md5
# from lib.jhash import file_to_md5
"""

import base64
import hashlib
import random

random = random.SystemRandom()


def string_to_md5(content):
    """Calculate the md5 hash of a string.

    This 'string' can be the binary content of a file too."""
    content = content.encode("utf8")
    return hashlib.md5(content).hexdigest()


def file_to_md5(filename, block_size=8192):
    """Calculate the md5 hash of a file. Memory-friendly solution,
    it reads the file piece by piece.

    https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python"""
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits.

    Taken from the django.utils.crypto module.
    """
    return ''.join(random.choice(allowed_chars) for i in range(length))


def get_secret_key():
    """
    Create a random secret key.

    Taken from the Django project.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)


def str2num(s):
    """
    from http://benkurtovic.com/2014/06/01/obfuscating-hello-world.html
    """
    codes = [ord(c) for c in s]
    num = sum(codes[i] * 256 ** i for i in range(len(codes)))
    return num


def num2str(n):
    """
    from http://benkurtovic.com/2014/06/01/obfuscating-hello-world.html
    """
    if n:
        return chr(n % 256) + num2str(n // 256)
    else:
        return ""


def str_to_base64(s):
    """
    >>> str_to_base64("László")
    'TMOhc3psw7M='
    """
    data = base64.b64encode(s.encode())
    return data.decode()


def base64_to_str(b64):
    """
    >>> base64_to_str("TMOhc3psw7M=")
    'László'
    """
    return base64.b64decode(b64.encode()).decode()

#############################################################################

if __name__ == "__main__":
    text = 'uncrackable12'  # :)
    print(string_to_md5(text))
    #
    filename = '/usr/bin/bash'
    print(file_to_md5(filename))

    print(string_to_md5(input("Word to md5: ")))

    s = get_secret_key()
    n = str2num(s)
    print(n)
    print(num2str(n))
