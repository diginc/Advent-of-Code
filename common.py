import pathlib
def read_input(file):
    f = pathlib.Path(file)
    return f.read_text()