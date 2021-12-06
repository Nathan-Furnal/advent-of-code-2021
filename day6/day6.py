from pathlib import Path

path = Path("input.txt")

with open(path, 'r') as f:
    data = list(map(int, f.readline().strip().split(",")))


def n_fishes(data: list[int], n_days: int, n_states=9):
    states = [0] * n_states
    for val in data:
        states[val] += 1
    for _ in range(n_days):
        nb_zeros = states[0]
        states = states[1:] + [nb_zeros]
        states[6] += nb_zeros
    return sum(states)


# Part 1

print(n_fishes(data, 80))

# Part 2

print(n_fishes(data, 256))
