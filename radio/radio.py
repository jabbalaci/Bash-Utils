#!/usr/bin/env python3

"""
Play online radio stations
==========================

Requirement: /usr/bin/mplayer

Last update: 2023-04-24 (yyyy-mm-dd)
"""

import os
import readline
import sys
from pathlib import Path

PLAYER = "/usr/bin/mplayer"
STATIONS = "stations.csv"


def read_data():
    """Read the input .csv file."""
    li = []
    dic = {}
    with open(STATIONS, "r") as f:
        for index, line in enumerate(f):
            li.append(line.rstrip("\n").split(";"))
            dic[li[-1][0]] = index

    return li, dic


def print_list(li):
    """Print station list to user."""
    print("Jabba's Minimalistic Radio Player :)")
    print("Media player:", PLAYER)
    print()
    for index, e in enumerate(li):
        pos = index + 1
        print("({pos}) {id:20}[{url}]".format(pos=pos, id=e[0], url=e[1]))


def read_choice(li, dic):
    """Read user's choice and return the selected record."""
    print()
    print("You can quit with 'q'.")
    while True:
        record = None
        try:
            choice = input("> ")
        except:
            print()
            exit(0)
        #
        if choice == "" or choice == "q":
            exit(0)
        # else
        try:
            # if it's a number
            if str(int(choice)) == choice:
                choice = int(choice)
        except ValueError:
            pass

        try:
            if isinstance(choice, int) and choice > 0:
                record = li[choice]
            elif isinstance(choice, str):
                record = li[dic[choice]]
        except IndexError:
            pass
        except KeyError:
            pass

        if record:
            break

    return record


def play_record(record):
    """Play station URL with mplayer."""
    station_url = record[1]
    cmd = "{player} '{url}'".format(player=PLAYER, url=station_url)
    os.system(cmd)


def check_player(prg):
    return Path(prg).is_file()


def main():
    """Controller."""
    li, dic = read_data()
    print_list(li[1:])
    record = read_choice(li, dic)
    play_record(record)


#############################################################################

if __name__ == "__main__":
    if check_player(PLAYER):
        main()
    else:
        print("Error: the media player '{0}' was not found".format(PLAYER))
        sys.exit(1)
