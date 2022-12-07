import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 7

def main(input):
    p1 = None
    p2 = None

    print(f"Day {DAY} Part 1: {p1}")
    print(f"Day {DAY} Part 2: {p2}")


if __name__ == '__main__':
    split_input = read_input(f"inputs/day{DAY}.txt", split='\n')
    raw_input = read_input(f"inputs/day{DAY}.txt", split='\n')

    header = np.loadtxt(f'inputs/day{DAY}.txt', max_rows=1, dtype=int, delimiter=',')
    remainder = np.loadtxt(f'inputs/day{DAY}.txt', skiprows=1, dtype=int)

    main(split_input)
