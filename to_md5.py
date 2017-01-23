#!/usr/bin/env python3

"""
Convert a text (string) to md5 hexa string.
"""

from lib.jhash import string_to_md5


def main():
    try:
        text = input("text> ")
    except (KeyboardInterrupt, EOFError):
        print()
        return
    #
    print("Text: '{}'".format(text))
    print()
    print(string_to_md5(text))

##############################################################################

if __name__ == "__main__":
    main()
