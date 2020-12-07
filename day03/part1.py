with open('input.txt', 'r') as fd:
    data = fd.read().splitlines()

open_squares = 0
tree_squares = 0
x = 0

for entry in data[1:]:
    x += 3

    remainder = x / 30
    if remainder >= 1:
        entry = entry * int(remainder + 1)

    if entry[x] == '.':
        open_squares += 1
    elif entry[x] == '#':
        tree_squares += 1

print(tree_squares)
