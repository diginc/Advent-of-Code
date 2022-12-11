import pytest
from numpy import np


DAY = 9

def main(data):
    print(f"Hello data! {data}")


test = read_input(f'inputs/test{DAY}.txt', split='\n')
real = read_input(f'inputs/day{DAY}.txt', split='\n')


@pytest.mark.parametrize('name, args, answer', [
    ('Test P1', (test), None),
    ('Test P2', (test), None),
    ('Real P1', (real), None),
    ('Real P2', (real), None),
])
def test_main(name, args, answer):
    result = main(*args)
    print(f"{name} result: {result}")
    if answer is not None:
        assert result == answer
    else:
        assert False, f"No answer given to prevent regression for {name}"