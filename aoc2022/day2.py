
def day2(input, title):
    input_list = input.split('\n')
    p1_foo = 0  # Same as "aim" For Part 2
    p1_bar = 0
    p2_foo = 0
    p2_bar = 0
    for line in input_list:
        line_list = line.split(' ')

    # Is that your final answer
    p1_answer = p1_foo * p1_bar
    p2_answer = p2_foo * p2_bar
    print(f"{title} Part 1: {p1_answer}")
    print(f"{title} Part 2: {p2_answer}")