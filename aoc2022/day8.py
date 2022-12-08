import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 8

data = read_input(f"inputs/day{DAY}.txt", split=False)
print('raw', data)
data = read_input(f"inputs/day{DAY}.txt", split='\n')
print('split', data)
data = np.loadtxt(f'inputs/day{DAY}.txt', max_rows=1, dtype=int, delimiter=',')
print('head', data)
data = np.loadtxt(f'inputs/day{DAY}.txt', skiprows=1, dtype=int)
print('rest', data)

p1 = None
p2 = None

print(f"Day {DAY} Part 1: {p1}")
print(f"Day {DAY} Part 2: {p2}")