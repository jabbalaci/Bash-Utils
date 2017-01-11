#!/usr/bin/env python3

"""
OCR with the Tesseract engine from Google
this is a wrapper around pytesser (http://code.google.com/p/pytesser/)
"""

import config as cfg
from lib.process import get_simple_cmd_output


def image_file_to_string(fname):
    """Convert an image file to text using OCR."""
    cmd = "{tesseract} {fname} stdout".format(
        tesseract=cfg.TESSERACT,
        fname=fname
    )
    return get_simple_cmd_output(cmd).rstrip('\n')
