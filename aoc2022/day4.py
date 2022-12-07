import re
import math
from common import *
from pprint import pprint

DAY = 4

def main(input):
    full_overlaps = 0
    any_overlaps = 0
    for elf in input:
        split = elf.dirname().split(',')
        parsed_ranges = [None, None]
        parsed_ranges[0] = [int(r) for r in split[0].split('-')]
        parsed_ranges[1] = [int(r) for r in split[1].split('-')]
        a = [r for r in range(parsed_ranges[0][0], parsed_ranges[0][1]+1)]
        b = [r for r in range(parsed_ranges[1][0], parsed_ranges[1][1]+1)]
        a_start, a_end = (a[0], a[-1])
        b_start, b_end = (b[0], b[-1])
        if (a_start in b and a_end in b) or (b_start in a and b_end in a):
            full_overlaps += 1
        if (a_start in b or a_end in b) or (b_start in a or b_end in a):
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
