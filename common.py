import pathlib
import sys
import numpy as np


def read_input(file, split='\n'):
    f = pathlib.Path(file)
    if not f.exists():
        print(f"Bad input: {f}")
        sys.exit(1)
    return_me = f.read_text()
    if split:
        return_me = return_me.strip().split(split)
    return return_me


def get_chararray(filename, **kwargs):
    '''
    each character of the file will be returned as a numpy 2d array

    Looked a little into char array under numpy but
    they didn't work while I was rushing to solve night of
    and this did work
    '''
    grid = np.array([], **kwargs)
    input = read_input(filename)
    x_size = -1
    y_size = len(input)
    for line in input:
        row = [int(t) for t in line]
        x_size = len(row)
        grid = np.append(grid, row)
    return np.reshape(grid, (x_size, y_size))
