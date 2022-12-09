import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

# Setup
DAY = 8


def main(grid, answers=None):
    ''' `grid` is data to solve today and optionally `answers` for refactor regression test '''
    x_size, y_size = grid.shape
    p1_trees = 0
    p2_score = 0
    debug = [(3, 2)]
    for x in range(x_size):
        for y in range(y_size):
            # Part 1
            loc = (x, y)
            height = grid[loc]
            if loc in debug:
                print(f"X: {x} Y: {y} is {height}")
            up = grid[:x, y]
            right = grid[x, y + 1:]
            down = grid[x + 1:, y]
            left = grid[x, :y]
            direction_visibility_checks = [
                (left < height).all(),
                (up < height).all(),
                (right < height).all(),
                (down < height).all()
            ]
            if np.any(direction_visibility_checks):
                p1_trees += 1

            # Part 2
            look_directions = [
                np.flip(up), np.flip(left),  # Same as up[::-1], left[::-1],
                right, down
            ]
            if loc in debug:
                print(look_directions)
            score = 1
            score_logger_debug = []
            for look_dir in look_directions:
                dir_score = 0
                for tree in look_dir:
                    dir_score += 1
                    if tree >= height:
                        break
                score_logger_debug.append(dir_score)
                score *= dir_score
            p2_score = max(score, p2_score)

    print(f"Day {DAY} Part 1: {p1_trees}")
    print(f"Day {DAY} Part 2: {p2_score}")
    if answers:
        assert p1_trees == answers[0]
        assert p2_score == answers[1]


test = file_to_byte_matrix(f"inputs/test{DAY}.txt", dtype=int)
main(test, answers=(21, 8))
real = file_to_byte_matrix(f"inputs/day{DAY}.txt", dtype=int)
main(real, answers=(1698, 672280))
