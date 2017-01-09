#!/usr/bin/env python3

"""
Interacting with processes.

Last update: 2017-01-08 (yyyy-mm-dd)
"""

import shlex
from subprocess import call, PIPE, Popen, STDOUT


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """Execute a simple external command and get its output.

    The command contains no pipes. Error messages are
    redirected to the standard output by default.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0].decode("utf8")


def execute_cmd(cmd):
    """Execute a simple external command."""
    args = shlex.split(cmd)
    call(args)

#############################################################################

if __name__ == "__main__":
    execute_cmd("date")
    s = get_simple_cmd_output("whoami").strip()
    print(s)
