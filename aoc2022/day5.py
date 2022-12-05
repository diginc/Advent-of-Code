import copy
import re
from common import *


DAY = 5
# original manual entered solution
# CRATES = [
#     ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'],
#     ['Z', 'C', 'D'],
#     ['H', 'J', 'F', 'C', 'N', 'G', 'W'],
#     ['P', 'J', 'D', 'M', 'T', 'S', 'B'],
#     ['N', 'C', 'D', 'R', 'J'],
#     ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'],
#     ['P', 'Z', 'T', 'F', 'R', 'H'],
#     ['L', 'V', 'M', 'G'],
#     ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J'],
# ]


def main(moves, crates):
    p1_crates = copy.deepcopy(crates)
    p2_crates = copy.deepcopy(crates)
    for line in moves:
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
    raw_crates, moves = read_input(f"inputs/day{DAY}.txt", split='\n\n')
    col_size = 4
    split_crates = raw_crates.split('\n')
    stack_count = len(split_crates[0]) // col_size
    crates = [[] for c in range(stack_count+1)]
    for line in split_crates:
        for m in re.finditer('[A-Z]', line):
            stack = m.start() // col_size
            crates[stack].insert(0, m.group())

    main(moves.split('\n'), crates)
