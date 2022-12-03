from common import *

DAY = 3
map = {
  "foo": "bar",
}


def main(input):
    input_list = input.split('\n')

    p1_answer = 0
    p2_answer = 0

    for line in input_list:
        win = False
        draw = False
        foo, bar = line.split(' ')

    # Is that your final answer
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


if __name__ == '__main__':
    main(read_input(f"day{DAY}.txt"))