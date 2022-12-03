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
    badges = []
    buffer = []
    for line in input:
        # Part 1
        size = len(line)
        half = (size/2)
        c1 = [val for i, val in enumerate(line) if i < half]
        c2 = [val for i, val in enumerate(line) if i >= half]
        for char in c1:
            if char in c2:
                dupes.append(char)
                break
        # Part 2
        buffer.append(line)
        if len(buffer) == 3:
            for char in buffer[0]:
                if char in buffer[1] and char in buffer[2]:
                    badges.append(char)
                    buffer = []
                    break


    for d in dupes:
        score = get_score(d)
        p1_answer += score

    for d in badges:
        score = get_score(d)
        p2_answer += score



    # Is that your final answer
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


def get_score(d):
    offset = 0
    if re.match('[a-z]', d):
        offset = -96
    if re.match('[A-Z]', d):
        offset = -38
    score = ord(d) + offset
    return score


if __name__ == '__main__':
    # Priority math
    assert ord('a') - 96 == 1
    assert ord('z') - 96 == 26
    assert ord('A') - 64 + 26 == 27
    assert ord('Z') - 64 + 26 == 52

    main(read_input(f"day{DAY}.txt", True))