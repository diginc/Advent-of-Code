import copy
import re
import numpy as np
import pandas as pd
from common import *
from pprint import pprint
from pathlib import  Path
import base64



DAY = 7
data = read_input(f"inputs/day{DAY}.txt", split='\n')

def get_path(p):
    return p.root if not p.name else p.resolve()

tree = {}
p = Path('/')
root = get_path(p)

for i, line in enumerate(data):
    if line.startswith('$ cd'):
        dirname = line.strip('$ cd')
        if p is None:
            p = Path(dirname)
        else:
            p = Path(Path(p, dirname).resolve())
            path = get_path(p)
            if path not in tree:
                tree[path] = {'size': 0, 'data': []}
    elif line.startswith('$ ls'):
        path = get_path(p)
    else:
        a, b = re.match('(.+) (.*)', line).groups()
        if a != 'dir':  # Then size
            tree[path]['size'] += int(a)
            parent = copy.deepcopy(p)
            while get_path(parent) != root:
                parent = Path(parent.parent)
                tree[get_path(parent)]['size'] += int(a)

less_than_100k = [v['size'] for k, v in tree.items() if v['size'] <= 100000]

print(sum(less_than_100k))

free_space = 70000000 - tree[root]['size']
best_size = 30000000 - free_space
delete_for_update_dirs = [dirs['size'] for k, dirs in tree.items() if dirs['size'] >= best_size]
options = sorted(delete_for_update_dirs)
print(options[0], options[-1])




