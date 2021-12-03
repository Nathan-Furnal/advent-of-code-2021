from pathlib import Path

path = Path("input.txt")
with open(path, 'r') as f:
    data = [l.strip() for l in f.readlines()]

N_BITS = len(data[0])

# Part 1


def compute_consumption(data):
    sums = list(map(int, data[0]))
    for line in data[1:]:
        line = list(map(int, line))
        for idx, val in enumerate(line):
            sums[idx] += val
    sums = list(map(lambda x: x / len(data), sums))
    gammas = list(map(round, sums))
    epsilons = [1 - x for x in gammas]
    gamma = '0b' + ''.join(str(i) for i in gammas)
    epsilon = '0b' + ''.join(str(i) for i in epsilons)
    return (gamma, epsilon, int(gamma, 2) * int(epsilon, 2))


gamma, epsilon, solution1 = compute_consumption(data)

# Part 2


def avg_bit(data):
    total = 0
    n = len(data)
    for val in data:
        total += int(val)
    avg = total / n
    avg_bit = 1 if avg >= .5 else 0
    return avg_bit


def compute_rating(data):
    oxy_rate = "0"
    co2_rate = "0"
    data_copy = data
    for i in range(N_BITS):
        oxy_bit = avg_bit([item[i] for item in data])
        data = [item for item in data if item[i] == str(oxy_bit)]
        if len(data) == 1:
            oxy_rate = data[0]
            break
    for i in range(N_BITS):
        co2_bit = 1 - avg_bit([item[i] for item in data_copy])
        data_copy = [item for item in data_copy if item[i] == str(co2_bit)]
        if len(data_copy) == 1:
            co2_rate = data_copy[0]
            break
    oxy_rate = int(oxy_rate, 2)
    co2_rate = int(co2_rate, 2)
    return (oxy_rate, co2_rate, oxy_rate * co2_rate)


print(compute_rating(data))
