import copy
import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

DAY = 6


def fishies_p1(data, days):
    data = data.copy()
    for z in range(days):
        new = len(data[data == 0])
        data -= 1
        data[data < 0] = 6
        data = np.append(data, [8] * new)
    return data


test = len(fishies_p1(np.array([3, 4, 3, 1, 2]), 80))
assert test == 5934
data = np.loadtxt(f'inputs/day{DAY}.txt', dtype=int, delimiter=',')
p1 = len(fishies_p1(data, 80))
print(f"Day {DAY} Part 1: {p1}")


'''
Actually having to optimize code??? AMAZING 
'''
def fishies_p2(data, days):
    fishes = []
    for i in range(9):
        fishes.insert(i, len([f for f in data if f == i]))

    for z in range(days):
        old_fishes = copy.deepcopy(fishes)
        for i in reversed(range(9)):
            if i != 0:
                fishes[i-1] = old_fishes[i]
            else:
                fishes[6] += old_fishes[0]
                fishes[8] = old_fishes[0]  # new

    return fishes


test18 = fishies_p2([3, 4, 3, 1, 2], 18)
test = sum(test18)
assert test == 26
test = sum(fishies_p2([3, 4, 3, 1, 2], 80))
assert test == 5934
test = sum(fishies_p2([3, 4, 3, 1, 2], 256))
assert test == 26984457539
data = np.loadtxt(f'inputs/day{DAY}.txt', dtype=int, delimiter=',').tolist()
p2 = sum(fishies_p2(data, 256))
print(f"Day {DAY} Part 2: {p2}")


# colections.deque.rotate(-1) would've been neater