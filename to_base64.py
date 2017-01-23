#!/usr/bin/env python3

"""
Convert a text (string) to a base64 string (encode).
"""

import readline    # to overcome the 4k input limit

from lib.jhash import str_to_base64


def main():
    try:
        text = input("text> ")
    except (KeyboardInterrupt, EOFError):
        print()
        return
    #
    print("Text: '{}'".format(text))
    print()
    print(str_to_base64(text))

##############################################################################

if __name__ == "__main__":
    main()
