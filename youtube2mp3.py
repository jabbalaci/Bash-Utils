#!/usr/bin/env python3

"""
Grab a youtube video in mp3.

Usage:
    youtube2mp3 VIDEO_URL
"""

import os
import sys

import config as cfg
from lib import fs
from lib.process import get_simple_cmd_output

fs.check_if_available(cfg.YOUTUBE_DL, "Error: {} is not available!".format(cfg.YOUTUBE_DL))
fs.check_if_available(cfg.FFMPEG, "Error: {} is not available!".format(cfg.FFMPEG))

# 96 kbit/s – generally used for speech or low-quality streaming
# 128 or 160 kbit/s – mid-range bitrate quality
AUDIO_QUALITY = "64K"    # I found it OK for speech


def process(url):
    cmd = 'youtube-dl -x --audio-format mp3 --audio-quality {bitrate} "{url}"'.format(bitrate=AUDIO_QUALITY,
                                                                                      url=url)
    print('#', cmd)
    os.system(cmd)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: provide a YouTube URL as a parameter!", file=sys.stderr)
        exit(1)
    # else
    process(sys.argv[1])
