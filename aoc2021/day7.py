import copy
import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 7

def main(grid, answers=None):
    p1 = None
    p2 = None
    print(f"Day {DAY} Part 1: {p1}")
    print(f"Day {DAY} Part 2: {p2}")
    if answers:
        assert p1 == answers[0]
        assert p2 == answers[1]




data = np.loadtxt(f'inputs/day{DAY}.txt', max_rows=1, dtype=int, delimiter=',')
data = np.loadtxt(f'inputs/day{DAY}.txt', skiprows=1, dtype=int)
data = read_input(f"inputs/day{DAY}.txt", split=False)
data = read_input(f"inputs/day{DAY}.txt", split='\n')

main(data, answers=None)