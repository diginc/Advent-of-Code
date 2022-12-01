import pathlib

def read_input(file):
    f = pathlib.Path(file)
    return f.read_text()


def day1a(input):
    elves = input.strip().split('\n\n')
    elves_inventories = [e.strip().split('\n') for e in elves]
    most_cals = 0
    for elf in elves_inventories:
        print(f"What ya got {elf}")
        cals = sum([int(c) for c in elf])
        if cals > most_cals:
            print(f"New most: {most_cals} {elf}")
            most_cals = cals
        else:
            print("Not most")

    print(f"Most calories an elf has: {most_cals}")


def day1b(input):
    elves = input.strip().split('\n\n')
    elves_inventories = [e.strip().split('\n') for e in elves]
    all_cals = []
    for elf in elves_inventories:
        cals = sum([int(c) for c in elf])
        all_cals.append(cals)

    top_3_cals = sorted(all_cals)[-3:]
    print(f"Most calories an elf has x3: {top_3_cals} = {sum(top_3_cals)}")


if __name__ == '__main__':
    day_filter = "1"
    part_filter = "b"
    p = pathlib.Path()
    for input in p.glob(f"input/day{day_filter}{part_filter}.txt"):
        func = input.name.replace(".txt", "")
        eval(func)(read_input(input))

