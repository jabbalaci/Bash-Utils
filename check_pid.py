#!/usr/bin/env python3

"""
Check a process ID (PID). If it's not running anymore, play a sound file.

Last update: 2024-12-21 (yyyy-mm-dd)
"""

import os
import sys
from pathlib import Path
from time import sleep

import psutil

WAIT = 3  # sec
ALERT = "assets/alert.wav"


def play_alert():
    cmd = "mplayer {0} 1>/dev/null 2>&1".format(ALERT)
    os.system(cmd)


def check_process(pid_to_check: int) -> None:
    while True:
        found = False
        for proc in psutil.process_iter(["pid", "name", "memory_info"]):
            try:
                pid = proc.info["pid"]
                name = proc.info["name"]
                memory = proc.info["memory_info"].rss / (1024 * 1024)  # in MB

                if pid == pid_to_check:
                    found = True
                    print(f"PID: {pid:<6} | Name: {name:<30} | Memory: {memory:.2f} MB")
                    break
                #
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            #
        #
        if not found:
            break
        #
        sleep(WAIT)
    #
    play_alert()


def main():
    if len(sys.argv) != 2:
        print("Usage: {0} <PID>".format(Path(sys.argv[0]).name))
        sys.exit(1)
    # else
    pid = int(sys.argv[1])
    check_process(pid)


##############################################################################

if __name__ == "__main__":
    main()
