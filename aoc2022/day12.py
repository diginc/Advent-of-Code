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


MOVE_MAP = {
    'D': (-1, 0),
    'U': (1, 0),
    'R': (0, 1),
    'L': (0, -1),
    '-1,0': 'D',
    '1,0': 'U',
    '0,1': 'R',
    '0,-1': 'L',
}


@dataclass
class Mountaineer:
    """
        The Mountaineer holds all his self location, map, and routing path data/notes
        They walk all the paths so you don't have to and finds the best one to a goal.
    """


    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data
        self.start = (self.x, self.y)
        self.last_loc = (self.x, self.y)
        self.elevation = height_map[self.data[(0, 0)]],
        self.route_plans = []
        self.dead_ends = []

    def coords(self) -> tuple:
        return self.x, self.y

    def adjacent(self) -> list:
        """ Adjacent squares without rolling over to other side of grid
        do: Add removal of already explored squares (NOT SCOUTED, VISITED) """
        valid_routes = [
            [coord, merge_coords(self.coords(), coord, self.data)]
            for coord in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            if merge_coords(self.coords(), coord, self.data) != self.coords()
        ]
        return valid_routes

    def map_routes(self, goal):
        """ Walk one route at a time until we reach our goal with some guess work to hope we go the right way
            Note all branches in the path for later review
            Re-traverse from earlier branching routes until you feel confident the best path is found"""
        for route in self.route_plans:
            next_steps = self.map_routes(route)
            self.route_plans.append([step for step in next_steps])
            del route

    def map_route(self, route):
        """ find the possible routes from current location that don't reverse course to previously visited locations """
        routes = []
        for route in self.adjacent():
            offset = route[0]
            full_coord = route[1]
            offset_str = ','.join([str(offset[0]), str(offset[1])])
            direction = MOVE_MAP[offset_str]
            print(f"{route} {direction}")



def loc_printer(pos, data):
    value = data[pos[0][0], pos[1][0]][0]
    print(f"{pos[0][0]}, {pos[1][0]} = {value}")

def get_np_tuple(pos, data):
    value = data[(pos[0][0], pos[1][0])]
    return pos[0][0], pos[1][0], value




def merge_coords(a, b, data):
    x = a[0] + b[0]
    y = a[1] + b[1]
    if x < 0: x = 0
    if x > len(data[0]): x = len(data[0])
    if y < 0: y = 0
    if y > len(data[1]): y = len(data[1])
    return x, y

def main(data):
    print()
    # print(f"heights {height_map}")
    pos = np.where(data == "S")
    end = np.where(data == "E")
    print("Start", get_np_tuple(pos, data))
    print("End", get_np_tuple(end, data))
    climber = Mountaineer(x=pos[0][0], y=pos[1][0], data=data)
    climber.map_routes(goal=end)


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
