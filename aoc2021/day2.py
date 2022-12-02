
def day2(input, title):
    input_list = input.split('\n')
    p1_depth = 0  # Same as "aim" For Part 2
    p1_horiz = 0
    p2_depth = 0
    p2_horiz = 0
    for d in input_list:
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
    # Is that your final answer
    p1_answer = p1_horiz * p1_depth
    p2_answer = p2_horiz * p2_depth
    print(f"{title} Part 1: {p1_answer}")
    print(f"{title} Part 2: {p2_answer}")