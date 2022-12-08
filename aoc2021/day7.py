import re
import copy
import numpy as np
import pandas as pd
from common import *
from pprint import pprint


DAY = 7


crabs = np.loadtxt(f'inputs/day{DAY}.txt', dtype=int, delimiter=',')
p1, p2 = None, None
print(f"Day {DAY} Part 1: {p1}")
print(f"Day {DAY} Part 2: {p2}")