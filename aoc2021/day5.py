import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

DAY = 5

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
        src, dst = sorted([[x1, y1], [x2, y2]])
        while src != dst:
            x, y = src
            y_offset = 1
            if dst[1] < src[1]:
                y_offset = -1
            grid[x, y] += 1
            src[0] += 1
            src[1] += y_offset

# FAILING no time before 2022 left
print(np.count_nonzero(grid >= 2))