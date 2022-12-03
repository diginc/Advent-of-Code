from common import *

DAY = 1


def main(input):
    input_ints = [int(i) for i in input]
    prev = []
    p1_increases = 0
    p2_increases = 0
    for line in input_ints:
        if prev and line > prev[-1]:
            p1_increases = p1_increases+1
        if len(prev) == 3:
            old_window = prev[0:3]
            cur_window = prev[1:3] + [line]
            if sum(cur_window) > sum(old_window):
                p2_increases = p2_increases+1
            prev.pop(0)
        prev.append(line)
    assert p1_increases == 1195
    assert p2_increases == 1235
    print(f"Day {DAY} Part 1: {p1_increases}")
    print(f"Day {DAY} Part 2: {p2_increases}")


if __name__ == '__main__':
    main(read_input(f"inputs/day{DAY}.txt", split='\n'))