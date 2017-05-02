#!/usr/bin/env python3

"""
A very basic solution to prettify a JSON file.
Usage:
    prettyjson.py ugly.json

A better way is to use jq at https://stedolan.github.io/jq/ .
Usage of jq:
    cat ugly.json | jq
"""

import json
import sys
from pathlib import Path


def beautify(fname):
    """
    Beautify the content of the file and return it as a string.
    """
    try:
        with open(fname) as f:
            d = json.load(f)
    except FileNotFoundError:
        print("Error: cannot open the input file.", file=sys.stderr)
        exit(1)
    except json.decoder.JSONDecodeError as e:
        print("Error: there is something wrong with this file.", file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)
    #
    return json.dumps(d, indent=2)

##############################################################################

if __name__ == "__main__":
    try:
        fname = sys.argv[1]
    except IndexError:
        p = Path(sys.argv[0])
        print("Usage: {} ugly.json".format(p.name), file=sys.stderr)
        exit(1)
    #
    print(beautify(fname))
