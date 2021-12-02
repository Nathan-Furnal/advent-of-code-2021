from pathlib import Path

path = Path("input2.txt")


def compute_depth_h_pos(path: Path):
    h_pos = depth = aim = 0

    with open(path, 'r') as f:
        for line in f:
            direction, val = line.split()
            if direction == "down":
                aim += int(val)
            elif direction == "up":
                aim -= int(val)
            else:
                h_pos += int(val)
                depth += aim * int(val)

    return h_pos * depth


print(compute_depth_h_pos(path))
