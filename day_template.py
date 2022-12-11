import copy
import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 9

def main(grid, answers=None):
    p1 = None
    p2 = None
    print(f"Day {DAY} Part 1: {p1}")
    print(f"Day {DAY} Part 2: {p2}")
    if answers:
        assert p1 == answers[0]
        assert p2 == answers[1]


test = f'inputs/test{DAY}.txt'
real = teat
data = np.loadtxt(test, max_rows=1, dtype=int, delimiter=',')
data = np.loadtxt(teat, skiprows=1, dtype=int)
data = read_input(test, split=False)
data = read_input(test, split='\n')
main(data, answer=())