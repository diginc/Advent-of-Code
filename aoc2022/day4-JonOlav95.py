'''
NOT MINE - FROM https://github.com/JonOlav95/advent_of_code_2022/blob/master/day_4/day_4.py
Wanted to run through debugger and check out internals of pandas/numpy closer
'''
import numpy as np
import pandas as pd


def split_to_range(x):
    start, stop = x.split("-")
    return range(int(start), int(stop) + 1)


def func(x, mode):
    r_1 = split_to_range(x[0])
    r_2 = split_to_range(x[1])

    if mode == "intersection":
        return bool(set(r_1).intersection(r_2))
    elif mode == "subset":
        return set(r_1).issubset(r_2) or set(r_2).issubset(r_1)

    return -1


def part_1(arr):
    result = np.apply_along_axis(func, -1, arr, "subset")
    subset_sum = result.sum()
    print(subset_sum)


def part_2(arr):
    result = np.apply_along_axis(func, -1, arr, "intersection")
    intersection_sum = result.sum()
    print(intersection_sum)


def main():
    df = pd.read_csv("inputs/day4.txt", header=None)
    arr = df.values

    part_1(arr)
    part_2(arr)


if __name__ == "__main__":
    main()