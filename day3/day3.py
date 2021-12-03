from pathlib import Path

path = Path("input.txt")

# Part 1


def compute_consumption(path: Path):
    l_counter = 0
    with open(path, 'r') as f:
        sums = list(map(int, f.readline().strip()))
        l_counter += 1
        for line in f:
            line = list(map(int, line.strip()))
            for idx, val in enumerate(line):
                sums[idx] += val
            l_counter += 1
    sums = list(map(lambda x: x / l_counter, sums))
    gammas = list(map(round, sums))
    epsilons = [1 - x for x in gammas]
    gamma = int('0b' + ''.join(str(i) for i in gammas), 2)
    epsilon = int('0b' + ''.join(str(i) for i in epsilons), 2)
    return gamma * epsilon


# Part 2
