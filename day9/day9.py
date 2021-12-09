from pathlib import Path
from functools import reduce
import operator as op

path = Path("input.txt")

with open(path, 'r') as f:
    data = []
    for line in f:
        data.append([*map(int, line.strip())])


# Part 1

def window(n: int, k: int, pos: tuple[int, int]) -> list[tuple[int, int]]:
    out = []
    i, j = pos
    if i - 1 >= 0:
        out.append((i - 1, j))
    if i + 1 < n:
        out.append((i + 1, j))
    if j - 1 >= 0:
        out.append((i, j - 1))
    if j + 1 < k:
        out.append((i, j + 1))
    return out

def find_low_points(data: list[list[int]])-> list[tuple[int, int]]:
    out = []
    n = len(data)
    k = len(data[0])
    for i in range(n):
        for j in range(k):
            curr = data[i][j]
            if all(data[pos[0]][pos[1]] > curr for pos in window(n, k, (i, j))):
                out.append((i, j))
    return out

print(sum(data[pos[0]][pos[1]] + 1 for pos in find_low_points(data)))
            
            
# Part 2

def recur_find_points(data: list[list[int]], p: tuple[int, int], points: set):
    n = len(data)
    k = len(data[0])
    i, j = p
    if i - 1 >= 0 and data[i-1][j] != 9 and (temp := (i - 1, j)) not in points:
        points.update([temp])
        recur_find_points(data, temp, points)
    if i + 1 < n and data[i+1][j] != 9 and (temp := (i + 1, j)) not in points:
        points.update([temp])
        recur_find_points(data, temp, points)
    if j - 1 >= 0 and data[i][j-1] != 9 and (temp := (i, j - 1)) not in points:
        points.update([temp])
        recur_find_points(data, temp, points)
    if j + 1 < k and data[i][j+1] != 9 and (temp := (i, j + 1)) not in points:
        points.update([temp])
        recur_find_points(data, temp, points)
    else: return points

    return points

def find_basins_size(data):
    low_points = find_low_points(data)
    basins = []
    for point in low_points:
        s = set()
        basins.append(recur_find_points(data, point, s))
    return basins

print(reduce(op.mul, sorted(map(len, find_basins_size(data)))[-3:]))

