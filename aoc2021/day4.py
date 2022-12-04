import re
from common import *
from pprint import pprint
import numpy as np
DAY = 4

CLEARED = [None]*5


def main(input):
    wins = setup_wins()
    balls, boards = process_input(input)
    for b, ball in enumerate(balls):
        pprint(f"Ball {ball}")
        for board in boards:
            for row in board:
                col = row.index(ball) if ball in row else None
                if col is not None:
                    row[col] = None

        # Debug
        # if b % 10 == 0:
        #     pprint(boards[0])
        #     pprint(np.transpose(boards[0]))

        # Part 1
        winner = False
        for board in boards:
            board = np.array(board)
            transpose = np.transpose(board)
            everything = []
            everything.append(np.array(np.diag(board)).tolist())
            everything.append(np.fliplr(board).diagonal().tolist())
            everything += [row.tolist() for row in board]
            everything += [col.tolist() for col in board]
            for check in everything:
                if None in check:
                    debug = True
                if check == CLEARED:
                    winner = True
        if winner:
            break
    debug = True

def process_input(input):
    balls = []
    boards = [[]]  # Start with empty board for later
    for line in input:
        if not balls:
            balls = [int(i) for i in line.strip().split(',')]
        else:
            if not line:
                continue
            if len(boards[-1]) == 5:  # prev board full, new board
                boards.append([])
            split = re.split(r'\s+', line.strip())
            split = [int(c) for c in split]
            boards[-1].append(split)
    return balls, boards


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
    main(read_input(f"inputs/day{DAY}.txt", split='\n'))
