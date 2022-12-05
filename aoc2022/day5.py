import copy
import re
from common import *


DAY = 5
CRATES = [
    ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'],
    ['Z', 'C', 'D'],
    ['H', 'J', 'F', 'C', 'N', 'G', 'W'],
    ['P', 'J', 'D', 'M', 'T', 'S', 'B'],
    ['N', 'C', 'D', 'R', 'J'],
    ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'],
    ['P', 'Z', 'T', 'F', 'R', 'H'],
    ['L', 'V', 'M', 'G'],
    ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J'],
]


def main(input):
    p1_crates = copy.deepcopy(CRATES)
    p2_crates = copy.deepcopy(CRATES)
    for line in input:
        mv_num, frm, to = re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
        mv_num = int(mv_num)
        frm = int(frm) - 1
        to = int(to) - 1

        # Part 1
        p1_mv = []
        for i in range(mv_num):
            p1_mv.append(p1_crates[frm].pop())
        p1_crates[to] += p1_mv

        # Part 2
        p2_mv = p2_crates[frm][-mv_num:]
        del p2_crates[frm][-mv_num:]
        p2_crates[to] += p2_mv

    p1_answer = ''
    p2_answer = ''
    for stack in p1_crates:
        p1_answer += stack[-1]
    for stack in p2_crates:
        p2_answer += stack[-1]
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


if __name__ == '__main__':
    split_input = read_input(f"inputs/day{DAY}.txt", split='\n')
    main(split_input)
