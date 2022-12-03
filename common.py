import pathlib


def read_input(file, split=False):
    f = pathlib.Path(file)
    return_me = f.read_text()
    if split:
        return_me = return_me.strip().split('\n')
    return return_me