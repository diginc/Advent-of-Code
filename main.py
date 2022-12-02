import pathlib

# Import all days imported into __init__ (ALL FUNCTIONS)
input_path = "aoc2022"
from aoc2022 import *

def read_input(file):
    f = pathlib.Path(file)
    return f.read_text()

if __name__ == '__main__':
    day_filter = "[2-25]"
    p = pathlib.Path()
    for input in p.glob(f"{input_path}/day{day_filter}.txt"):
        func = input.name.replace(".txt", "")
        title = func.replace("day", "Day ")
        eval(func)(read_input(input), title)

