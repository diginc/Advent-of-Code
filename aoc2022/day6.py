import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint

DAY = 6


data = read_input(f"inputs/day{DAY}.txt", split=False)

for i in range(4, len(data)):
    last_4 = data[i-3:i+1]
    last_4_unique = set(c for c in last_4)
    if len(last_4_unique) == 4:
        print(i+1, last_4_unique)
        break


for i in range(14, len(data)):
    last_14 = data[i-13:i+1]
    last_14_unique = set(c for c in last_14)
    if len(last_14_unique) == 14:
        print(i+1, last_14_unique)
        break