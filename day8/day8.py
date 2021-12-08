from pathlib import Path

path = Path("input.txt")

uniq_segments = {1: 2, 4: 4, 7: 3, 8: 7}
in_uniques = lambda x: x in set(uniq_segments.values())

with open(path, 'r') as f:
    data = []
    for line in f:
        line = line.strip()
        inp, out = map(lambda x: x.strip().split(), line.split("|"))
        data.append([inp, out])

# Part 1

def count_uniqs(data):
    count = 0
    for elem in data:
        count += len([*filter(in_uniques, map(len, elem[1]))])
    return count

print(count_uniqs(data))

# Part 2

# Logic with sets
## A candidate is a set with the correct number of segments
### Order of conditions is important

# 0: left from 6: and 9:
# 1: Unique with 2 segments
# 2: left from 3: and 5:
# 3: (Candidate - 1) -> 3 segments left
# 4: Unique with 4 segments
# 5: (candidate - 4) -> 2 segments left
# 6: (8 - candidate) intersect 1
# 7: Unique with 3 segments
# 8: Unique with 7 segments
# 9: (Candidate - 4) -> 2 segments left

def mapping(inp: list, out: list) -> str:
    d = {}
    inp = sorted(inp, key=len)
    # unique values
    d[inp[0]] = "1"
    d[inp[1]] = "7"
    d[inp[2]] = "4"
    d[inp[9]] = "8"
    # rules
    for s in inp[3:6]: # candidates for 2 3 5
        if len(set(s) - set(inp[0])) == 3:
            d[s] = "3"
        elif len(set(s) - set(inp[2])) == 2:
            d[s] = "5"
        else:
            d[s] = "2"
    for s in inp[6:9]: # candidates for 0 6 9
        if len(set(s) - set(inp[2])) == 2:
            d[s] = "9"
        elif (set(inp[9]) - set(s)).intersection(set(inp[0])):
            d[s] = "6"
        else:
            d[s] = "0"
    sol = ""
    for st in out:
        sol += d["".join(i for i in d.keys() if set(i) == set(st))]
    return sol

def sums(data):
    total = 0
    for elem in data:
        total += int(mapping(*elem))
    return total

print(sums(data))
        
