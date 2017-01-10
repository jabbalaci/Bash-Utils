#!/usr/bin/env python3

"""
Play a sound when the Internet connection is back.
"""

import os
import socket
from pathlib import Path
from time import sleep

from lib import network
from lib.audio import play

ROOT = os.path.dirname(os.path.abspath(__file__))
TIMEOUT = 3
AUDIO = str(Path(ROOT, "assets", "alert.wav"))


def main():
    cnt = 0
    while True:
        cnt += 1
        print('# testing...' if cnt == 1 else '# test again...')
        if network.is_internet_on(method=3):
            print('# Whoa, your net is alive!')
            play(AUDIO)
            play(AUDIO)
            play(AUDIO)
            break
        else:
            print('# no connection, waiting...')
            sleep(10)

#############################################################################

if __name__ == "__main__":
    socket.setdefaulttimeout(TIMEOUT)
    main()
