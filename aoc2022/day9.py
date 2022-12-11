import copy
import re

import numpy
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

DAY = 9
DIR_MAP = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}
FOLLOWMAP = [
    [[-1, -1], [-1, -1], [-1, 0], [-1, 1], [-1, 1]],
    [[-1, -1], [0, 0],   [0, 0],  [0, 0],  [-1, 1]],
    [[0, -1],  [0, 0],   [0, 0],  [0, 0],  [0, 1]],
    [[1, -1],  [0, 0],   [0, 0],  [0, 0],  [1, 1]],
    [[1, -1],  [1, -1],  [1, 0],  [1, 1],  [1, 1]]
]

AXIS_MAP = {
    'R': 1,
    'L': 1,
    'U': 0,
    'D': 0,
}
MOVE_MAP = {
    'R': 1,
    'L': -1,
    'U': -1,
    'D': 1,
}

def update_coord(t, m):
    return [t[0] + m[0], t[1] + m[1]]


def main(moves, length=2, answers=None):
    # Just make a huge grid, start in middle
    debug = range(10)
    # debug = [0, 8]
    start = [500, 500]
    visited = set()
    knots = [copy.deepcopy(start) for _ in range(length)]
    for direction, distance in moves:
        # xy = AXIS_MAP[direction]
        print('-' * 20)
        distance = int(distance)
        for di in range(distance):
            prefix = f"{direction} {di + 1}/{distance}"
            for k in range(len(knots) - 1):
                leader = knots[k]
                follow = knots[k + 1]
                axis_a = AXIS_MAP[direction]
                if k == 0:
                    leader[axis_a] += MOVE_MAP[direction]
                    print(f"{prefix} LEADER_{k}[{axis_a}] = {leader}")
                print(f"FOLLOW LOC {leader} - {follow}")
                fm_loc = [leader[0] - follow[0]+2, leader[1] - follow[1]+2]
                print(f"FOLLOW WORK {fm_loc}")
                follow[0] += FOLLOWMAP[fm_loc[0]][fm_loc[1]][0]
                follow[1] += FOLLOWMAP[fm_loc[0]][fm_loc[1]][1]

                if tuple(knots[-1]) not in visited:
                    print(f"VISITED ============ {tuple(knots[-1])}")
                    visited.add(tuple(knots[-1]))

    if answers[0]:
        p1 = len(visited)
        print(f"Day {DAY} Part 1: {p1}")
        assert p1 == answers[0]
    if answers[1]:
        p2 = len(visited)
        print(f"Day {DAY} Part 2: {p2}")
        assert p2 == answers[1]


test = [line.split(' ') for line in read_input(f"inputs/test{DAY}.txt")]
main(test, length=2, answers=(13, None))
real = [line.split(' ') for line in read_input(f"inputs/day{DAY}.txt")]
main(real, length=2, answers=(6494, None))

test = [line.split(' ') for line in read_input(f"inputs/test{DAY}.txt")]
main(test, length=10, answers=(1, None))
test2 = [line.split(' ') for line in read_input(f"inputs/test{DAY}b.txt")]
main(test2, length=10, answers=(None, 36))
real = [line.split(' ') for line in read_input(f"inputs/day{DAY}.txt")]
main(real, length=10, answers=(None, 2691))
