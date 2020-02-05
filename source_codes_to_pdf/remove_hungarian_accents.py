#!/usr/bin/env python3

import sys

csere = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ö': 'o',
    'ő': 'o',
    'ú': 'u',
    'ü': 'u',
    'ű': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ö': 'O',
    'Ő': 'O',
    'Ú': 'U',
    'Ü': 'U',
    'Ű': 'U',
}

def main(fname):
    try:
        with open(fname) as f:
            content = f.read()
    except:
        print("Warning: problem with the file", fname)
        raise
    #
    for k, v in csere.items():
        content = content.replace(k, v)
    #
    print(content)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {0} <input_file>".format(sys.argv[0]))
        exit(1)
    # else
    main(sys.argv[1])
