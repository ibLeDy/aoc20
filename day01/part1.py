with open('input.txt', 'r') as fp:
    data = list(map(int, fp.read().splitlines()))

for entry in data:
    difference = 2020 - entry
    if difference in data:
        print(entry * difference)
        break
