from pathlib import Path

path = Path("input.txt")

with open(path, 'r') as f:
    data = list(map(int, f.readline().strip().split(",")))


def n_fishes(data: list[int], n_days: int, n_states: int = 9) -> int:
    states = [0] * n_states  # [0:8] possible values
    for val in data:
        states[val] += 1  # set the initial states
    for _ in range(n_days):
        # get the number of zeros for a given day
        nb_zeros = states[0]
        # shift every value left and make states[0] -> states[-1]
        states = states[1:] + [nb_zeros]
        # Spawn new fishes any time zeros are shifted left (they start at value 6)
        states[6] += nb_zeros
    return sum(states)


# Part 1

print(n_fishes(data, 80))

# Part 2

print(n_fishes(data, 256))
