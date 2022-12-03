import copy
import re
from common import *

DAY = 3
first_bit_map = {
  "foo": "bar",
}


def main(raw_input):
    input = raw_input.split('\n')
    gamma = ""
    epsilon = ""
    lsr = None
    ogr = None

    data = process_data(input)
    for char_i in data:
        majority = 0
        minority = 1
        if char_i >= len(input)/2:
            majority = 1
            minority = 0
        gamma += str(majority)
        epsilon += str(minority)

    # majority = gamma[0]
    # minority = epsilon[0]
    # char_i = 0
    # lsr_data = copy.deepcopy(input)
    # ogr_data = copy.deepcopy(input)
    # while len(lsr_data) != 1 and len(ogr_data) != 1:
    #     prefix = char_i * '\d'
    #     maj_pattern = f"^{prefix}{majority}\d*"
    #     min_pattern = f"^{prefix}{minority}\d*"
    #     char_i += 1
    #     lsr_data = re.findall(maj_pattern, '\n'.join(lsr_data))
    #     lsr_sum = process_data(lsr_data)
    #     majority = 0
    #     if lsr_sum[char_i] >= len(lsr_data)/2:
    #         print(lsr_data)
    #         majority = 1
        
        #ogr_data = re.findall(min_pattern, '\n'.join(ogr_data))

    p1_answer = int(gamma, 2) * int(epsilon, 2)
    assert p1_answer == 2648450  # Don't break things
    p2_answer = 0 # int(lsr, 2) * int(ogr, 2)

    # Is that your final answer
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


def process_data(input):
    data = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in input:
        for slot in range(len(input[0])):
            data[slot] += int(line[slot])
    return data

if __name__ == '__main__':
    main(read_input(f"day{DAY}.txt"))