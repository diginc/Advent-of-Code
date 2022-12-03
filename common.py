import pathlib
import sys


def read_input(file, split='\n'):
    f = pathlib.Path(file)
    if not f.exists():
        print(f"Bad input: {f}")
        sys.exit(1)
    return_me = f.read_text()
    if split:
        return_me = return_me.strip().split(split)
    return return_me
