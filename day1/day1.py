from pathlib import Path
from collections import deque

path = Path("input.txt")

# Part 1


def delta_counter(path: Path):
    counter = 0
    with open(path, "r") as f:
        curr = int(f.readline())
        for line in f:
            val = int(line)
            if val > curr:
                counter += 1
            curr = val
    return counter


print(delta_counter(path))

# Part 2


def sliding_window_counter1(path: Path) -> int:
    counter = 0
    with open(path, 'r') as f:
        a, b, c = int(f.readline()), int(f.readline()), int(f.readline())
        sum_abc = a + b + c
        for line in f:
            a, b, c = b, c, int(line)
            new_sum = a + b + c
            if new_sum > sum_abc:
                counter += 1
            sum_abc = new_sum
    return counter


print(sliding_window_counter1(path))


def sliding_window_counter2(path: Path) -> int:
    counter = 0
    with open(path, 'r') as f:
        data = f.readlines()
        for curr, futur in zip(data, data[3:]):
            if int(curr) < int(futur):
                counter += 1
    return counter


print(sliding_window_counter2(path))


def sliding_window_counter3(path: Path) -> int:
    counter = 0
    with open(path, 'r') as f:
        a, b, c = int(f.readline()), int(f.readline()), int(f.readline())
        queue = deque([a, b, c])
        for line in f:
            curr = queue.popleft()
            if curr < int(line):
                counter += 1
            queue.append(int(line))
    return counter


print(sliding_window_counter3(path))
