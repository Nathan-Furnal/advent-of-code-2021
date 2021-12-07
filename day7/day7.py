from pathlib import Path
from statistics import median, mean
import math

path = Path("input.txt")

with open(path, 'r') as f:
    data = list(map(int, f.readline().strip().split(",")))

# Part 1


def fuel_cost(data):
    med = median(data)
    return int(sum(abs(i - med) for i in data))


print(fuel_cost(data))

# Part 2


def cost(dist):
    return int(dist * (dist + 1) / 2)


def sum_cost(arr, val):
    return sum(cost(abs(elem - val)) for elem in arr)


def fuel_cost2(data):
    window = int(len(data) * .1)
    m = round(mean(data))
    minim = sum_cost(data, m)
    for i in range(m - window, m + window):
        if (temp := sum_cost(data, i)) < minim:
            minim = temp
    return minim


print(fuel_cost2(data))
