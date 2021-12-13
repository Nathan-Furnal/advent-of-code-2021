from pathlib import Path
path = Path("input.txt")

def read_input(path):
    data = path.read_text().strip().split("\n")
    points = set()
    folds = []
    for line in data:
        if line != '':
            if not line.startswith("fold"):
                points.add(tuple(map(int, line.split(","))))
            else:
                val = line.split(" ")[-1]
                if val[0] == 'x':
                    folds.append((int(val.split("=")[-1]), 0))
                else:
                    folds.append((0, int(val.split("=")[-1])))
    return points, folds

points, folds = read_input(path)

# Part 1

def dots(points, folds):
    dots = []
    for fold in folds:
        fx, fy = fold
        s = set()
        for point in points:
            x, y = point
            if fy != 0 and y > fy:
                y = fy - abs(y - fy)
                s.add((x, y))
            elif fx != 0 and x > fx:
                x = fx - abs(x - fx)
                s.add((x, y))
            else:
                s.add(point)
        dots.append(s)
        points = s
    return dots

print(len(dots(points, folds)[0]))

# Part 2

def make_string(points):
    s = ""
    x_min = min(points, key = lambda x : x[0])[0]
    y_min = min(points, key = lambda x : x[1])[1]
    x_max = max(points, key=lambda x : x[0])[0]
    y_max = max(points, key=lambda x : x[1])[1]
    for i in range(y_min, y_max + 1):
        for j in range(x_min, x_max + 1):
            if (j, i) in points:
                s += "#"
            else: s += "."
        s += "\n"
    return s

print(make_string(dots(points, folds)[-1]))
