import copy
import re
from common import *
from pprint import pprint
import numpy as np


DAY = 4
CLEARED = np.array(['X']*5)

def check_bingo(hits):
    return np.any([
        np.all(hits[0, :]),
        np.all(hits[1, :]),
        np.all(hits[2, :]),
        np.all(hits[3, :]),
        np.all(hits[4, :]),
        np.all(hits[:, 0]),
        np.all(hits[:, 1]),
        np.all(hits[:, 2]),
        np.all(hits[:, 3]),
        np.all(hits[:, 4]),
    ])

def main(balls, boards):
    p1 = None
    p2 = None
    hits = np.zeros(boards.shape, dtype=int)
    trash_i = []
    for ball in balls:
        for board_i, board in enumerate(boards):
            if board_i in trash_i:
                continue
            indices = np.where(board == ball)
            if len(indices[0]) > 0:
                x = indices[0][0]
                y = indices[1][0]
                hits[board_i][x][y] = 1
                if check_bingo(hits[board_i]):
                    trash_i.append(board_i)
                    # PART 1
                    if not p1:
                        numbers_left = np.ma.masked_array(board, mask=hits[board_i])
                        p1 = np.sum(numbers_left) * ball
                        print(f"Day {DAY} Part 1: {p1}")
                    # PART 2 Go till end
                    if len(trash_i) == len(boards):
                        numbers_left = np.ma.masked_array(board, mask=hits[board_i])
                        p2 = np.sum(numbers_left) * ball
                        print(f"Day {DAY} Part 2: {p2}")
                        return  # Stop processing early


def setup_wins():
    wins = []
    diag = []
    for i in range(5):
        diag.append([i, i])  # Diagonal
        horz = []
        vert = []
        for j in range(5):
            horz.append([i, j])
            vert.append([j, i])
        wins.append(horz)
        wins.append(vert)
    wins.append(diag)
    return wins


if __name__ == '__main__':
    balls = np.loadtxt(f'inputs/day{DAY}.txt', max_rows=1, dtype=int, delimiter=',')
    boards = np.loadtxt(f'inputs/day{DAY}.txt', skiprows=1, dtype=int)
    boards = np.reshape(boards, (-1, 5, 5))
    main(balls, boards)
