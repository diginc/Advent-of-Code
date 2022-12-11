import copy
import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 10
CYCLE_MAP = {
    'addx': 2,
    'noop': 1,
}
DEBUG = False

def part1(data, answer=None):
    watch_for = [20] + [i for i in range(60, 1000)[::40]]
    interesting = []
    if DEBUG: print(watch_for)
    c = 0
    x = 1
    for line in data:
        op = 'noop'
        val = 0
        if line != 'noop':
            op, val = line.split(' ')
        if DEBUG: print(f"{op}: {val}")
        if c + CYCLE_MAP[op] >= watch_for[0]:
            signal = x * watch_for[0]
            if DEBUG: print(f"{c} + {CYCLE_MAP[op]} will pass {watch_for[0]} - Interesting!  {x} * {watch_for[0]} = {signal}")
            interesting.append(copy.deepcopy(signal))
            watch_for.pop(0)
        c += CYCLE_MAP[op]
        x += int(val)
        if DEBUG: print(f"cycle {c} ends with x {x} and {interesting}")
    p1 = sum(interesting)

    if answer:
        print(f"Day {DAY} Part 1: {p1}")


def part2(data):
    watch_for = [20] + [i for i in range(60, 10000)[::40]]
    interesting = []
    crt_picture = []
    crt_line = []
    c = 1
    x = 1
    for line in data:
        op = 'noop'
        val = 0
        if line != 'noop':
            op, val = line.split(' ')
        if DEBUG: print(f"{op}: {val}")
        for i in range(CYCLE_MAP[op]):
            offset = len(crt_picture) * 40
            sprite = [x+offset, x+1+offset, x+2+offset]
            if DEBUG: print(f"{c} in {sprite}")
            if c in sprite:
                crt_line.append('#')
            else:
                crt_line.append('.')
            if len(crt_line) == 40:
                crt_picture.append(crt_line)
                if DEBUG: print(''.join(crt_line))
                crt_line = []
            c += 1
            if DEBUG: print(f"cycle {c} ends with x {x} and {crt_line}")
        x += int(val)
    for l in crt_picture:
        print(''.join(l))


test = f'inputs/test{DAY}.txt'
data = read_input(test)
part1(data, 13140)
part2(data)

real = f'inputs/day{DAY}.txt'
data = read_input(real)
part1(data, 13520)
part2(data)
