import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


# Setup
DAY = 8
filename = f"inputs/test{DAY}.txt"
filename = f"inputs/day{DAY}.txt"
grid = np.array([], dtype=int)
x_size = 0
input = read_input(filename)
y_size = len(input)
for line in input:
    row = [int(t) for t in line]
    x_size = len(row)
    grid = np.append(grid, row)

grid = np.reshape(grid, (x_size, y_size))

p1_trees = 0
p2_score = 0
debug = [(3, 2)]
for x in range(x_size):
    for y in range(y_size):
        # Part 1
        loc = (x, y)
        height = grid[loc]
        # print(f"X: {x} Y: {y} is {height}")
        # print(x, y, '=', height, grid[:x, y])  #, grid[x, :y], grid[x + 1:, y], grid[x, y + 1:])
        up = grid[:x, y]
        right = grid[x, y + 1:]
        down = grid[x + 1:, y]
        left = grid[x, :y]
        visible = [
            (left < height).all(),
            (up < height).all(),
            (right < height).all(),
            (down < height).all()
        ]
        if np.any(visible):
            p1_trees += 1

        # Part 2 could be coolers with slice iteration [::1] probably
        score = 1
        score_logger_debug = []
        if loc in debug:
            score_logger_debug = []
        for look_dir in [
            np.flip(up), np.flip(left),
            right, down
        ]:
            dir_score = 0
            for tree in look_dir:
                dir_score += 1
                if tree >= height:
                    break
            score_logger_debug.append(dir_score)
            score *= dir_score
        p2_score = max(score, p2_score)
        # if y in [0, y_size] or x in [0, x_size]:
        #     print(score_logger_debug, score)

print(f"Day {DAY} Part 1: {p1_trees}")
print(f"Day {DAY} Part 2: {p2_score}")

if 'test' in filename:
    assert p1_trees == 21
    assert p2_score == 8
else:
    assert p1_trees == 1698
    assert p2_score != 5762400