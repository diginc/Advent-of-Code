from common import read_input

DAY = 1


def main(input):
    elves = input.strip().split('\n\n')
    elves_inventories = [e.strip().split('\n') for e in elves]
    all_cals = []
    for elf in elves_inventories:
        cals = sum([int(c) for c in elf])
        all_cals.append(cals)

    p1_answer = sorted(all_cals)[-1]
    p2_answer = sum(sorted(all_cals)[-3:])
    print(f"Day {DAY} Part 1: {p1_answer}")
    print(f"Day {DAY} Part 2: {p2_answer}")


if __name__ == '__main__':
    main(read_input(f"day{DAY}.txt"))