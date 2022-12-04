import re
import math
from common import *
from pprint import pprint

DAY = 4

def main(input):
    full_overlaps = 0
    any_overlaps = 0
    for i, elf in enumerate(input):
        ranges = [None, None]
        split = elf.strip().split(',')
        ranges[0] = [int(i) for i in split[0].split('-')]
        ranges[1] = [int(i) for i in split[1].split('-')]
        this_pair = []
        for j in range(2):
            j1 = ranges[j][0]
            j2 = ranges[j][1]
            exploded_ranges = [r for r in range(j1, j2+1)]
            this_pair.insert(j, exploded_ranges)
        if len(this_pair) == 2:
            a = this_pair[0]
            b = this_pair[1]
            if (a[0] in b and a[-1] in b) or (b[0] in a and b[-1] in a):
                full_overlaps += 1
            if (a[0] in b or a[-1] in b) or (b[0] in a or b[-1] in a):
                any_overlaps += 1

    p1_answer = full_overlaps
    p2_answer = any_overlaps
    assert p1_answer == 413
    assert p2_answer == 806
    # Is that your final answer
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")

if __name__ == '__main__':
    main(read_input(f"inputs/day{DAY}.txt", split='\n'))
