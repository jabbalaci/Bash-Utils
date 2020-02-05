Input: a bunch of source codes.

Output: a nice, formatted PDF containing all the source codes.
        The source codes are syntax highlighted.

-----

Found here:

https://superuser.com/questions/601198/how-can-i-automatically-convert-all-source-code-files-in-a-folder-recursively

Removing the Hungarian accents was added by me.

Current settings:

* syntax highlight for C files

* process `*.c` and `*.h` files.

Usage:

    $ ./src2pdf

Output: `all.pdf`
