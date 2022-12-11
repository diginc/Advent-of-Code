import copy
import math
from common import *
from dataclasses import dataclass
import pytest

DAY = 11


@dataclass()
class Monkey(object):
    id: int = None
    items: list = None
    item_count: int = 0
    op: None = None
    test: int = None
    true: int = None
    false: int = None

def monkey_factory(data):
    monkeys = []
    m = Monkey()
    for line in data:
        line = line.strip()
        s = line.split(' ')
        match s[0]:
            case "Monkey": m.id = int(s[1].strip(':'))
            case "Starting": m.items = [int(i.strip(',')) for i in s[2:]]
            case "Operation:":
                match s[4:]:
                    case ['+', 'old']: m.op = lambda x: x + x
                    case ['*', 'old']: m.op = lambda x: x * x
                    case ['+', d]: m.op = lambda x, y=int(d): x + y
                    case ['*', d]: m.op = lambda x, y=int(d): x * y
            case "Test:":
                assert s[1] == 'divisible', 'only coding for divisible tests, this should not fail'
                m.test = int(s[3])
            case "If":
                match s[1]:
                    case "true:": m.true = int(s[5])
                    case "false:":
                        m.false = int(s[5])
                        print(f"Recording monkey finished: {m}")
                        monkeys.append(m)
                        m = Monkey()
    return monkeys


def monkey_time(monkeys, rounds, div=1):
    for r in range(rounds):
        for monkey in monkeys:
            for i, item in enumerate(copy.deepcopy(monkey.items)):
                monkey.item_count += 1
                monkey.items[0] = monkey.op(item) // div
                if div != 3:
                    monkey.items[0] = monkey.op(item) % div
                test_result = monkey.items[0] % monkey.test
                if test_result == 0:
                    monkeys[monkey.true].items.append(monkey.items.pop(0))
                else:
                    monkeys[monkey.false].items.append(monkey.items.pop(0))
        if r+1 in [1, 20] + [i for i in range(1000, rounds+1)[::1000]]:
            for monkey in monkeys:
                print(f"{r+1} Monkey {monkey.id} {monkey.item_count}")

    return sorted([m.item_count for m in monkeys])


def main(data, rounds, div):
    monkeys = monkey_factory(data)
    if div is None:
        divisors = [m.test for m in monkeys]
        div = math.prod(divisors)
        print(f"ANTI STRESS PRESCRIBED: calculated a common divisor for all monkeys of prod({divisors}) = {div}")
    item_count = monkey_time(monkeys, rounds, div)
    print(item_count)
    answer = math.prod(item_count[-2:])
    return answer


test = read_input(f'inputs/test{DAY}.txt', split='\n')
real = read_input(f'inputs/day{DAY}.txt', split='\n')


@pytest.mark.parametrize('name, args, answer', [
    ('Test P1', (test, 20, 3), 10605),
    ('Test P2', (test, 10000, None), 2713310158),
    ('Real P1', (real, 20, 3), 101436),
    ('Real P2', (real, 10000, None), 19754471646),
])
def test_main(name, args, answer):
    result = main(*args)
    print(f"{name} result: {result}")
    if answer is not None:
        assert result == answer
    else:
        assert False, f"No answer given to prevent regression for {name}"