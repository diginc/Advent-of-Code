import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

DAY = 6


data = read_input(f"inputs/day{DAY}.txt", split=False)


def find_unique_char_set(num):
    global i
    for i in range(num, len(data)):
        beg = i - (num - 1)
        end = i + 1
        window = data[beg:end]
        unique = set(c for c in window)
        if len(unique) == num:
            print(i + 1)
            break

find_unique_char_set(4)
find_unique_char_set(14)

