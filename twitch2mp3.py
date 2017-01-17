#!/usr/bin/env python3

"""
Grab a twitch video in mp3.

Usage:
    twitch2mp3 VIDEO_URL
"""

import config as cfg
import os

from lib import fs, podium
from lib.process import get_simple_cmd_output

fs.check_if_available(cfg.YOUTUBE_DL, "Error: {} is not available!".format(cfg.YOUTUBE_DL))
fs.check_if_available(cfg.FFMPEG, "Error: {} is not available!".format(cfg.FFMPEG))


def slugify(text):
    text = text.replace('http://', '')
    text = text.replace('https://', '')
    text = text.replace('/', '_')
    text = text.replace('.', '_')
    return text


def main():
    url = input("URL of the twitch video: ")
    cmd = 'youtube-dl -g "{}"'.format(url)
    print('#', cmd)
    url2 = get_simple_cmd_output(cmd).strip()
    print('#', url2)
    cmd = 'ffmpeg -i "{video}" -f mp3 {audio}.mp3'.format(
        video=url2, audio=slugify(url)
    )
    print('#', cmd)
    os.system(cmd)

##############################################################################

if __name__ == "__main__":
    main()
