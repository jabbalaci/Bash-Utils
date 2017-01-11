#!/usr/bin/env python3

"""
Convert an image file to string.
"""

import sys

import config as cfg
from lib import fs, ocr

fs.check_if_available(cfg.TESSERACT, "Error: {} is not available!".format(cfg.TESSERACT))


def process(f):
    """
    Process each image file and OCR them. The result
    is printed to the stdout.
    """
    return ocr.image_file_to_string(f)

#############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Error: provide an image file.')
        sys.exit(1)
    # else
    for idx, f in enumerate(sys.argv[1:]):
        if idx > 0:
            print('-' * 10)
        print(process(f))
