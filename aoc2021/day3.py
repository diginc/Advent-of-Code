import copy
from common import *

DAY = 3
def main(raw_input):
    input = raw_input.split('\n')
    gamma = ""
    epsilon = ""
    data = process_data(input)
    for char_i in data:
        majority = 0
        minority = 1
        if char_i >= len(input)/2:
            majority = 1
            minority = 0
        gamma += str(majority)
        epsilon += str(minority)

    p1_answer = int(gamma, 2) * int(epsilon, 2)
    assert p1_answer == 2648450  # Don't break things
    print(f"Day {DAY} Part 1: {p1_answer}")

    # Part 2
    lsr_data = copy.deepcopy(input)
    ogr_data = copy.deepcopy(input)
    done = False
    while not done:
        for column in range(len(input[0])):
            if len(lsr_data) > 1:
                lsr_data = p2_processor(column, lsr_data, majority=True)

            if len(ogr_data) > 1:
                ogr_data = p2_processor(column, ogr_data, majority=False)
            #print(column, "OGR", len(ogr_data), "LSR", len(lsr_data))
            done = (len(lsr_data) == 1 and len(ogr_data) == 1)

    p2_answer = int(lsr_data[0], 2) * int(ogr_data[0], 2)
    print(f"Day {DAY} Part 2: {p2_answer}")

def p2_processor(column, data, majority=True):
    flipped_data = flip_data(data)
    zero_count = flipped_data[column].count(0)
    one_count = flipped_data[column].count(1)
    filter_for = 1 if zero_count <= one_count else 0
    if not majority:
        filter_for = 0 if zero_count <= one_count else 1
    filtered = [line for line in data if int(line[column]) == filter_for]
    return filtered

def process_data(input):
    data = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in input:
        for slot in range(len(input[0])):
            data[slot] += int(line[slot])
    return data

def flip_data(input):
    data = []
    for i, line in enumerate(input):
        for j, b in enumerate(line):
            if j > len(data) - 1:
                data.insert(j, [])
            data[j].insert(i, int(b))

    assert len(data[0]) == len(input), f"{len(data[0])} not {len(input)}"
    assert len(data) == len(input[0]), f"{len(data)} not {len(input[0])}"
    return data

if __name__ == '__main__':
    main(read_input(f"day{DAY}.txt"))