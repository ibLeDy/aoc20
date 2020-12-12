from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

    # I'm using the empty line ('') as the delimiter so
    # I have to manually add one at the end so the last
    # line won't get omitted.
    data.append('')

counts = list()
current_group_data = Counter()
group_members = 0
for line in data:
    if line == '':
        counts.append(
            len([i for i, j in current_group_data.items() if j == group_members])
        )
        current_group_data.clear()
        group_members = 0
    else:
        group_members += 1
        current_group_data += Counter(line)

print(sum(counts))
