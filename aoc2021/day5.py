import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

DAY = 5
# https://github.com/scottpenn/advent_of_code_2021/blob/main/days/day_05/solution.py Helped a lot
data = np.fromregex(f'inputs/day{DAY}.txt', '(\d*),(\d*) -> (\d*),(\d*)\n*',
                     [('x1', int), ('y1', int), ('x2', int), ('y2', int)])

grid = np.zeros((1000, 1000), dtype=int)

for x1, y1, x2, y2 in data:
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        for y in range(y1, y2+1):
            grid[x1, y] += 1
    elif y1 == y2:
        x1, x2 = sorted([x1, x2])
        for x in range(x1, x2+1):
            grid[x, y1] += 1

print(np.count_nonzero(grid >= 2))

grid = np.zeros((1000, 1000), dtype=int)
i = 0
for x1, y1, x2, y2 in data:
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        for y in range(y1, y2+1):
            grid[x1, y] += 1
    elif y1 == y2:
        x1, x2 = sorted([x1, x2])
        for x in range(x1, x2+1):
            grid[x, y1] += 1
    else:
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        while (x1, y1) <= (x2, y2):  # <= not == (Beware off by one)
            grid[x1, y1] += 1
            #print(x1, y1)
            x1 += 1
            if y2 > y1:
                y1 += 1
            else:
                y1 -= 1

p2 = np.count_nonzero(grid >= 2)
assert p2 == 20373
print(p2)