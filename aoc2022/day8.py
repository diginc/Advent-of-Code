import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


# Setup
DAY = 8
p1_trees = 0
p2_trees = 0
grid = np.array([], dtype=int)
for line in read_input(f"inputs/day{DAY}.txt"):
    grid = np.append(grid, [int(t) for t in line])

grid = np.reshape(grid, (99, 99))

p1_trees = 0
p2_score = 0
x_size = grid.shape[0]
y_size = grid.shape[1]
for x in range(x_size):
    for y in range(y_size):
        # Part 1
        loc = (x, y)
        height = grid[loc]
        if np.any([
            (grid[:x, y] < height).all(),
            (grid[x, :y] < height).all(),
            (grid[x + 1:, y] < height).all(),
            (grid[x, y + 1:] < height).all()
        ]):
            p1_trees += 1

        # Part 2
        score = 1
        n, e, s, w = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for d in [n, e, s, w]:
            dir_score = 0
            look = (loc[0] + d[0], loc[1] + d[1])
            while abs(look[0]) < x_size and abs(look[1]) < y_size:
                dir_score += 1
                if np.all(grid[look] > height):
                    break
                look = (look[0] + d[0], look[1] + d[1])
            score *= dir_score
            p2_score = max(score, p2_score)

print(f"Day {DAY} Part 1: {p1_trees}")
assert p1_trees == 1698
print(f"Day {DAY} Part 2: {p2_score}")