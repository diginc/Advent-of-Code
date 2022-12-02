
def day1(input, title):
    input_list = input.split('\n')
    input_ints = [int(i) for i in input_list]
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
    print(f"{title} Part 1: {p1_increases}")
    print(f"{title} Part 2: {p2_increases}")