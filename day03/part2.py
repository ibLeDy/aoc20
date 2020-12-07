import math
from collections import namedtuple

Slope = namedtuple('Slope', ['x', 'y'])
SLOPES = [
    Slope(1, 1),
    Slope(3, 1),
    Slope(5, 1),
    Slope(7, 1),
    Slope(1, 2),
]

with open('input.txt', 'r') as fd:
    data = fd.read().splitlines()

total_tree_squares = []
for slope in SLOPES:
    open_squares = 0
    tree_squares = 0
    x = 0

    for entry in data[slope.y::slope.y]:
        x += slope.x

        remainder = x / 30
        if remainder >= 1:
            entry = entry * int(remainder + 1)

        if entry[x] == '.':
            open_squares += 1
        elif entry[x] == '#':
            tree_squares += 1

    total_tree_squares.append(tree_squares)

print(math.prod(total_tree_squares))
