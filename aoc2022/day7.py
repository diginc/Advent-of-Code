import copy
import re
from common import *
from pathlib import Path

DAY = 7
data = read_input(f"inputs/day{DAY}.txt", split='\n')


def get_path(p):
    return p.root if not p.name else p.resolve()


tree = {}
p = Path('/')
root = get_path(p)

# Process into a flat tree of sizes
for i, line in enumerate(data):
    if line.startswith('$ cd'):
        directory = line.strip('$ cd')
        p = Path(Path(p, directory).resolve())
        path = get_path(p)
        if path not in tree:
            tree[path] = {'size': 0, 'data': []}
    else:
        a, b = re.match('(.+) (.*)', line).groups()
        if a.isnumeric():
            tree[path]['size'] += int(a)
            parent = copy.deepcopy(p)
            while get_path(parent) != root:
                parent = Path(parent.parent)
                tree[get_path(parent)]['size'] += int(a)

# Part 1
less_than_100k = [v['size'] for k, v in tree.items() if v['size'] <= 100000]
p1 = sum(less_than_100k)
assert p1 == 1367870
print(p1)

# Part 2
free_space = 70000000 - tree[root]['size']
best_size = 30000000 - free_space
delete_for_update_dirs = [dirs['size'] for k, dirs in tree.items() if dirs['size'] >= best_size]
p2 = sorted(delete_for_update_dirs)[0]
assert p2 == 549173
print(p2)
