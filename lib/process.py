#!/usr/bin/env python3

"""
Interacting with processes.
* launch a new process
* launch a new process and get its output
* launch a new process in the background

# from jplib import process
# from jplib.process import get_simple_cmd_output
# from jplib.process import get_exitcode_stdout_stderr
# from jplib.process import get_return_code_of_simple_cmd
"""

import os
import shlex
from subprocess import PIPE, STDOUT, Popen, call
from time import sleep

import psutil


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """Execute a simple external command and get its output.

    The command contains no pipes. Error messages are
    redirected to the standard output by default.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0].decode("utf8")


def get_complex_cmd_output(cmd, stderr=STDOUT):
    """
    Execute a piped command and get the lines of the output in a list.
    """
    proc = Popen(cmd, shell=True, stdout=PIPE, stderr=stderr)
    return proc.stdout.readlines()


def get_cmd_output_input_from_stdin(cmd, input_file):
    """Execute an external command and get its output. The command
    receives its input_file from the stdin through a pipe.

    Example: 'echo test | grep es'."""
    args = shlex.split(cmd)
    p = Popen(args, stdout=PIPE, stdin=PIPE)    # | grep es
    p.stdin.write(bytearray(input_file.encode("utf8")))                        # echo test |
    return p.communicate()[0].decode("utf8")


def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
    """Execute a simple external command and return its exit status."""
    args = shlex.split(cmd)
    return call(args, stdout=PIPE, stderr=stderr)


def get_exitcode_stdout_stderr(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    args = shlex.split(cmd)

    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    out, err = out.decode("utf8"), err.decode("utf8")
    exitcode = proc.returncode
    #
    return exitcode, out, err


def execute_cmd(cmd):
    """Execute a simple external command."""
    args = shlex.split(cmd)
    call(args)


def execute_cmd_in_background(cmd):
    """Execute a (shell) command in the background.

    Returns the process' pid."""
    #call("{0} &".format(cmd), shell=True)
    #http://stackoverflow.com/questions/1605520
    args = shlex.split(cmd)
    p = Popen(args)
    return p.pid


def get_process_list():
    """Get the list of running processes.

    Example:
        PROCNAME = "python.exe"

        for proc in psutil.process_iter():
            if proc.name == PROCNAME:
                proc.kill()
    """
    return psutil.process_iter()


def keep_alive(cmd):
    """
    Keep a process alive.

    If the process terminates, it will restart it.
    The terminated processes become zombies. They
    die when their parent terminates.
    """
    while True:
        pid = execute_cmd_in_background(cmd)
        p = psutil.Process(pid)
        while p.is_running() and str(p.status) != 'zombie':
#            print p
#            sleep(5)
            os.system('sleep 5')


def is_process_running(pname):
    """
    Is the given process running?

    pname is the process' name, e.g. 'firefox'
    """
    cmd = "ps ux | grep '{pname}' | grep -v grep".format(pname=pname)
    output = get_complex_cmd_output(cmd)
    if output:
        return True
    else:
        return False

#############################################################################

if __name__ == "__main__":
#     print(get_simple_cmd_output("echo -n Ubuntu"))
#     print(get_cmd_output_input_from_stdin("grep es", "test"))
#     print(get_return_code_of_simple_cmd("date"))
#     cmd = "/usr/bin/eog"
#     print('pid:', execute_cmd_in_background(cmd))
# #    li = get_process_list()
# #    for p in li:
# #        print p.pid
#     print(get_complex_cmd_output("cat /etc/passwd | head -1"))
#     print('__END__')
# #    keep_alive('/usr/bin/xclock')
    print(is_process_running('firefox'))
