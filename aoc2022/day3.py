import re
from common import *

DAY = 3
map = {
  "foo": "bar",
}




def main(input):
    p1_answer = 0
    p2_answer = 0

    dupes = []
    for line in input:

        size = len(line)
        half = (size/2)
        c1 = [val for i, val in enumerate(line) if i < half]
        c2 = [val for i, val in enumerate(line) if i >= half]
        for char in c1:
            if char in c2:
                dupes.append(char)
                break

    # Priority math
    assert ord('a') - 96 == 1
    assert ord('z') - 96 == 26
    assert ord('A') - 64 + 26 == 27
    assert ord('Z') - 64 + 26 == 52

    for d in dupes:
        offset = 0
        if re.match('[a-z]', d):
            offset = -96
        if re.match('[A-Z]', d):
            offset = -38
        score = ord(d) + offset
        p1_answer += score



    # Is that your final answer
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


if __name__ == '__main__':
    main(read_input(f"day{DAY}.txt", True))