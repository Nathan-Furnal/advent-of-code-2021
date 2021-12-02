from pathlib import Path

path = Path("input2.txt")

# Part 1


def compute_position(path: Path):
    h_pos = depth = 0
    d_moves = {
        "forward": lambda x: h_pos + x,
        "down": lambda x: depth + x,
        "up": lambda x: depth - x
    }

    with open(path, 'r') as f:
        for line in f:
            direction, val = line.split()
            if direction == "forward":
                h_pos = d_moves[direction](int(val))
            else:
                depth = d_moves[direction](int(val))

    return h_pos * depth


print(compute_position(path))

# Part 2


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
