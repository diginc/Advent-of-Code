import pytest
import numpy as np
from common import *
from dataclasses import dataclass
import string

DAY = 12
height_map = {v: k for (k, v) in enumerate(list(string.ascii_lowercase))}
height_map["S"] = 0
height_map["E"] = 25
test = file_to_byte_matrix(f'inputs/test{DAY}.txt')
real = file_to_byte_matrix(f'inputs/day{DAY}.txt')


@dataclass
class Mountaineer:
    elevation: int = 0
    x: int = 0
    y: int = 0
    visited: list = None

    def coords(self) -> tuple:
        return self.x, self.y


def loc_printer(pos, data):
    value = data[pos[0][0], pos[1][0]][0]
    print(f"{pos[0][0]}, {pos[1][0]} = {value}")


def merge_coords(a, b, data):
    x = a[0] + b[0]
    y = a[1] + b[1]
    if x < 0: x = 0
    if x > len(data[0]): x = len(data[0])
    if y < 0: y = 0
    if y > len(data[1]): y = len(data[1])
    return (x, y)

def main(data):
    print()
    print(f"heights {height_map}")
    pos = np.where(data == "S")
    end = np.where(data == "E")
    loc_printer(pos, data)
    loc_printer(end, data)
    climber = Mountaineer(
        elevation=height_map[data[(0, 0)]],
        x=pos[0][0],
        y=pos[1][0],
        visited=[],
    )
    print(climber)
    valid_paths = get_valid_paths(climber, data)
    for path in valid_paths:
        print(f"From  moves: {path} = {data[path]} / {height_map[data[path]]}")


def get_valid_paths(climber, data):
    valid_routes = [merge_coords(climber.coords(), coord, data)
                    for coord in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    if merge_coords(climber.coords(), coord, data) != climber.coords()]
    return valid_routes


if __name__ == '__main__':
    main(real)
    main(test)

# @pytest.mark.parametrize('name, args, answer', [
#     ('Real P1', real, 31),
#     ('Test P1', test, 31),
#     # ('Test P2', (test, None), None),
#     # ('Real P1', (real, None), None),
#     # ('Real P2', (real, None), None),
# ])
# def test_main(name, args, answer):
#     result = main(args)
#     print(f"{name} result: {result}")
#     if answer is not None:
#         assert result == answer
#     else:
#         assert False, f"No answer given to prevent regression for {name}"
