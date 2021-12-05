from pathlib import Path
from dataclasses import dataclass, field

path = Path("input.txt")

convert = lambda x: tuple(map(int, x.split(",")))
sign = lambda x: -1 if x < 0 else 1

with open(path, 'r') as f:
    data = []
    for line in f:
        line = list(map(lambda x: x.strip(), line.split("->")))
        x, y = map(convert, line)
        data.append((x, y))


@dataclass
class Point:
    x: int
    y: int
    marks: int = field(default=0, compare=False)

    def dist(self, other: Point = Point(0, 0)):  #type: ignore
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1 / 2)

    def copy(self):
        return Point(self.x, self.y)


@dataclass
class Segment:
    p1: Point
    p2: Point
    points: list[Point] = field(default_factory=list)

    def __post_init__(self):
        small_p = self.p1.copy(
        ) if self.p1.dist() <= self.p2.dist() else self.p2.copy()
        big_p = self.p1.copy(
        ) if self.p1.dist() > self.p2.dist() else self.p2.copy()
        dx = big_p.x - small_p.x
        dy = big_p.y - small_p.y
        while small_p != big_p:
            self.points.append(Point(small_p.x, small_p.y))
            if dx != 0 and small_p.x != big_p.x:
                small_p.x += 1 * sign(dx)
            if dy != 0 and small_p.y != big_p.y:
                small_p.y += 1 * sign(dy)
        self.points.append(big_p)


# Part 1

d_pos = {}

for coord1, coord2 in data:
    if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
        p1, p2 = Point(*coord1), Point(*coord2)
        s = Segment(p1, p2)
        for p in s.points:
            if d_pos.get((p.x, p.y), None) is None:
                d_pos[(p.x, p.y)] = 1
            else:
                d_pos[(p.x, p.y)] += 1

print(sum(val >= 2 for val in d_pos.values()))

# Part 2

d_pos = {}

for coord1, coord2 in data:
    p1, p2 = Point(*coord1), Point(*coord2)
    s = Segment(p1, p2)
    for p in s.points:
        if d_pos.get((p.x, p.y), None) is None:
            d_pos[(p.x, p.y)] = 1
        else:
            d_pos[(p.x, p.y)] += 1

print(sum(val >= 2 for val in d_pos.values()))
