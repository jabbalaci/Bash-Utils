#!/usr/bin/env python3

"""
Convert a base64 string back to a normal string (decode).
"""

from lib.jhash import base64_to_str as back


def main():
    try:
        inp = input("base64 string> ")
    except (KeyboardInterrupt, EOFError):
        print()
        return
    #
    print("Input: '{}'".format(inp))
    print()
    print(back(inp))

##############################################################################

if __name__ == "__main__":
    main()
