#!/usr/bin/env python3

"""
XML to JSON converter.
"""

import json
import sys

from lib import xmltodict


def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: {0} input.xml'.format(sys.argv[0]))
        sys.exit(1)
    # else
    print(convert(sys.argv[1]))
