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
import glob

from optparse import OptionParser
from datetime import datetime
from time import sleep


MUSIC_DIR = '/home/jabba/bin/alarm/at_a_given_time/assets'
MEDIA_PLAYER = '/usr/bin/mplayer'
DEFAULT_TIME = '6h55'


def play_music():
    #for f in sorted(glob.glob(os.path.join(MUSIC_DIR, '*.mp3'))):
    for f in sorted(glob.glob(os.path.join(MUSIC_DIR, '*.mp3'))):
        val = os.system("{0} {1}".format(MEDIA_PLAYER, f))
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
        if not ( (0 <= hour <= 23) and (0 <= minute <= 59) ):
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
                      help = 'Play music. Useful for adjusting the volume.')

    options, arguments = parser.parse_args()
    #print options
    #print arguments
    if options.is_play:
        play_music()    # play and
        sys.exit(0)     # quit
    # else
    if options.alarm_time:
        hour, minute = check_alarm(options.alarm_time)
        set_alarm(hour, minute)


if __name__ == "__main__":
    main()
