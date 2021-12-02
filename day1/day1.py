from pathlib import Path

path = Path("input1.txt")


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
