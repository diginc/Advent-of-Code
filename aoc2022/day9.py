import copy
import re

import numpy
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 9
DIRMAP = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}
FOLLOWMAP = {
    'L': (0, 1),
    'R': (0, -1),
    'D': (-1, 0),
    'U': (1, 0),
}
def update_coord(t, m):
    return (t[0] + m[0], t[1] + m[1])
def main(moves, answers=None):
    grid = np.zeros((750, 750))
    head = (grid.shape[0] // 2, grid.shape[1] // 2)
    tail = (grid.shape[0] // 2, grid.shape[1] // 2)
    for direction, distance in moves:
        distance = int(distance)
        print(direction, '=', distance)
        for i in range(distance):
            head = update_coord(head, DIRMAP[direction])
            ht_dist = [
                abs(head[0] - tail[0]),
                abs(head[1] - tail[1]),
            ]
            if ht_dist[0] > 1 or ht_dist[1] > 1:
                tail = copy.deepcopy(head)
                tail = update_coord(tail, FOLLOWMAP[direction])

            print(ht_dist)
            grid[tail] += 1
            print(grid)
            # if tail vs head > 1, trigger follow on same axis
            # if tail vs head > 1 on both x and y, follow in opposite of dirmap


    p1 = np.count_nonzero(grid >= 1)
    p2 = None
    print(f"Day {DAY} Part 1: {p1}")
    print(f"Day {DAY} Part 2: {p2}")

    if answers:
        assert p1 == answers[0]
        assert p2 == answers[1]



test = [line.split(' ') for line in read_input(f"inputs/test{DAY}.txt")]
real = [line.split(' ') for line in read_input(f"inputs/day{DAY}.txt")]
main(test, answers=(13, None))
main(real, answers=(6494, None))