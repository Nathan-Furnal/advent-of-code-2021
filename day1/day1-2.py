from pathlib import Path

path = Path("input1.txt")


def sliding_window_counter(path: Path) -> int:
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


print(sliding_window_counter(path))
