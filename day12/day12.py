"""
Not my own solution but rather https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/12.py
Trying to understand how to use graphs for the solution
"""

from pathlib import Path
from collections import defaultdict, deque
path = Path("input.txt")

def read_data(path):
    g = defaultdict(set)
    for line in path.read_text().strip().split("\n"):
        left, right = line.strip().split("-")
        g[left].add(right)
        g[right].add(left)
    return g

data = read_data(path)

# adjacency list - for each vertex, what vertices does it have edges to?
E = read_data(path)

def solve(p1):
    start = ('start', set(['start']), None)
    ans = 0
    Q = deque([start])
    while Q:
        # where we are, which small caves we've visited
        pos, small, twice = Q.popleft()
        if pos == 'end':
            ans += 1
            continue
        for y in E[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ['start', 'end'] and not p1:
                Q.append((y, small, y))
    return ans
print(solve(p1=True))
print(solve(p1=False))



