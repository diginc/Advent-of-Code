def day1(input, title):
    elves = input.strip().split('\n\n')
    elves_inventories = [e.strip().split('\n') for e in elves]
    all_cals = []
    for elf in elves_inventories:
        cals = sum([int(c) for c in elf])
        all_cals.append(cals)

    print(f"{title} Part 1, most cal elf: {all_cals[-1]}")
    top_3_cals = sorted(all_cals)[-3:]
    print(f"{title} Part 2, top 3 cal elves and their sum: {top_3_cals} = {sum(top_3_cals)}")