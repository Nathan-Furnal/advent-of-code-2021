from pathlib import Path

path = Path("input2.txt")


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
