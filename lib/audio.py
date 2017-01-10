#!/usr/bin/env python3

"""
Playing audio (and video too) files.

# from jplib import audio
"""

import os

import config as cfg


def play(audio_file, background=False, debug=False):
    """Play an audio file with mplayer."""
    cmd = '{player} "{audio}"'.format(player=cfg.PLAYER, audio=audio_file)
    if not debug:
        cmd += ' 1>/dev/null 2>&1'
    if background:
        cmd += ' &'
    os.system(cmd)
