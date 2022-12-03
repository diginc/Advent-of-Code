from common import *

DAY = 2


def main(input):
    p1_depth = 0  # Same as "aim" For Part 2
    p1_horiz = 0
    p2_depth = 0
    p2_horiz = 0
    for d in input:
        direct, amount = d.split(' ')
        amount = int(amount)
        if direct == "up":
            p1_depth -= amount
        if direct == "down":
            p1_depth += amount
        if direct == "forward":
            p1_horiz += amount
            p2_horiz += amount
            p2_depth += p1_depth * amount
    p1_answer = p1_horiz * p1_depth
    assert p1_answer == 1451208
    p2_answer = p2_horiz * p2_depth
    assert p2_answer == 1620141160
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


if __name__ == '__main__':
    main(read_input(f"inputs/day{DAY}.txt", split='\n'))
