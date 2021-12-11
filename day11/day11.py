from pathlib import Path
path  = Path("input.txt")

with open(path, 'r') as f:
    data = [list(map(int, line.strip())) for line in f.readlines()]

d = {"up" : (-1, 0), "down" : (1, 0), "left" : (0, -1), "right" : (0, 1),
     "upl": (-1, -1), "upr": (-1, 1), "downl": (1, -1), "downr" : (1, 1) }

N, K = len(data), len(data[0])

def flash(data, pos : tuple[int, int], positions : set[tuple[int, int]]) ->  set[tuple[int, int]]:
    x, y = pos
    if data[x][y] == 0:
        positions.update([(x, y)])
        for move in d.keys():
            dx, dy = d[move]
            xdx, ydy = x + dx, y + dy
            if (N > xdx >= 0) and (K > ydy >= 0) and (xdx, ydy) not in positions:
                data[xdx][ydy] = (data[xdx][ydy] + 1) % 10
                if data[xdx][ydy] == 0:
                    flash(data, (xdx, ydy), positions)
    return positions

# Part 1

def count_flashes(data: list[list[int]], n_steps : int) -> int:
    cnt = 0
    for _ in range(n_steps):
        positions = set()
        for i in range(N):
            for j in range(K):
                data[i][j] = (data[i][j] + 1) % 10
                flash(data, (i, j), positions)
                if (i, j) in positions:
                    data[i][j] = 0
        cnt += len(positions)
    return cnt

print(count_flashes(data, 100))

# Part 2

with open(path, 'r') as f:
    data = [list(map(int, line.strip())) for line in f.readlines()]
    
def sync_flashes(data: list[list[int]]) -> int:
    n_steps = 1
    while n_steps:
        positions = set()
        for i in range(N):
            for j in range(K):
                data[i][j] = (data[i][j] + 1) % 10
                flash(data, (i, j), positions)
                if (i, j) in positions:
                    data[i][j] = 0
        if len(positions) == N*K:
            return n_steps
        else: n_steps += 1
    return n_steps

print(sync_flashes(data))
