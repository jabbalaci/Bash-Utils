#!/usr/bin/env python

"""
Alarm script
============

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/04/17/alarm-script/
GitHub:  https://github.com/jabbalaci/Bash-Utils

A simple alarm script that plays a list of MP3s at a given time.
Very useful if you leave your computer switched on during the night.

Usage:
------

./alarm.py -p
    Play music. First do this to adjust volume! If the volume is low,
    you won't hear it in the morning.

./alarm.py -t 7h15
    Set alarm time. The format is HhM, where H is the hour (24-hour system),
    M is the minute, 'h' is the separator.

./alarm.py
    Set alarm with the default time. In my case it's 6h55.
"""

import os
import sys

from optparse import OptionParser
from datetime import datetime
from time import sleep
from random import shuffle


MUSIC_DIR = '/media/jabba/JIVE/mp3/sfa_scifi'
TRAVERSE_RECURSIVELY = True
MPLAYER = '/usr/bin/mplayer'
MPLAYER_OPTIONS = '-endpos 00:00:60'    # play first 60 seconds; disabled when -p is used
DEFAULT_TIME = '6h55'


class CollectMp3:
    """Collect music files recursively in a given directory."""
    def __init__(self, music_dir):
        self.music_dir = music_dir
        self.songs = []

    def traverse(self, directory):
        """Traverse directory recursively. Symlinks are skipped."""
        content = [os.path.join(directory, x) for x in os.listdir(directory)]
        dirs = sorted([x for x in content if os.path.isdir(x)])
        files = sorted([x for x in content if os.path.isfile(x)])

        for f in files:
            if os.path.islink(f):
                continue
            ext = os.path.splitext(f)[1]
            if ext in ('.mp3', '.flac', '.ogg', '.flv'):
                self.songs.append(f)

        if TRAVERSE_RECURSIVELY:
            for d in dirs:
                if os.path.islink(d):
                    continue
                self.traverse(d)

    def collect(self):
        """Collect songs, shuffle order, and print a little statistics."""
        self.traverse(self.music_dir)
        if self.get_number_of_songs() == 0:
            print "Error: there are no songs available."
            sys.exit(-1)
        # else
        shuffle(self.songs)
        header = "number of songs: {0}".format(self.get_number_of_songs())
        sep = '#' * (len(header) + 2 + 2)
        print sep
        print '# ' + header + ' #'
        print sep
        print

    def get_number_of_songs(self):
        return len(self.songs)

    def get_songs(self):
        return self.songs


collector = CollectMp3(MUSIC_DIR)

#############################################################################


def play_music():
    songs = collector.get_songs()
    for f in songs:
        val = os.system("{mplayer} {options} \"{song}\"".format(mplayer=MPLAYER, options=MPLAYER_OPTIONS, song=f))
        if val == 2:    # interrupted with CTRL-C
            sys.exit(val)


def set_alarm(hour, minute):
    # autoflush
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    sep = "=" * 19
    print sep
    print "| Alarm at {0:2}h{1:02}. |".format(hour, minute)
    print sep

    alarm_time = hour * 100 + minute

    while True:
        now = datetime.now()
        time = datetime.time(now)
        current_time = time.hour * 100 + time.minute
        if (current_time >= alarm_time) and (current_time - alarm_time <= 100):
            play_music()
            sys.exit(0)
        else:
            sys.stdout.write('.')
            try:
                sleep(10)
            except KeyboardInterrupt:
                print
                break   # break out of 'while True'


def check_alarm(alarm_time):
    msg = "{0} error: there is a problem with the alarm time.".format(sys.argv[0])
    try:
        alarm_time = alarm_time.lower()
        if 'h' not in alarm_time:
            alarm_time += 'h'
        hour, minute = alarm_time.split('h')
        if not minute:
            minute = '0'
        hour = int(hour)
        minute = int(minute)
        if not ((0 <= hour <= 23) and (0 <= minute <= 59)):
            print >>sys.stderr, msg
            sys.exit(1)
    except ValueError:
        print >>sys.stderr, msg
        sys.exit(1)

    return hour, minute


def main(default=DEFAULT_TIME):
    parser = OptionParser(usage='%prog [options]')

    #[options]
    parser.add_option('-t',
                      '--time',
                      action='store',
                      default=default,
                      type='string',
                      dest='alarm_time',
                      help='Alarm time, ex.: 6h55.')

    parser.add_option('-p',
                      '--play',
                      action='store_true',
                      default=False,
                      dest='is_play',
                      help='Play music. Useful for adjusting the volume.')

    options, arguments = parser.parse_args()

    if options.is_play:
        global MPLAYER_OPTIONS
        MPLAYER_OPTIONS = ''
        print '# MPLAYER_OPTIONS is disabled'

    collector.collect()

    if options.is_play:
        play_music()    # play and
        sys.exit(0)     # quit
    # else
    if options.alarm_time:
        hour, minute = check_alarm(options.alarm_time)
        set_alarm(hour, minute)


if __name__ == "__main__":
    main()
