import pathlib
import sys
import numpy as np


def read_input(file, split='\n'):
    f = pathlib.Path(file)
    if not f.exists():
        print(f"Bad input/could not find: {f}")
        sys.exit(1)
    return_me = f.read_text()
    if split:
        return_me = return_me.strip().split(split)
    return return_me


def file_to_byte_matrix(filename, **kwargs):
    """ each char/cell/byte of the homogeneously sized file will be returned as a numpy 2d array """
    return np.array([list(line) for line in read_input(filename)], **kwargs)