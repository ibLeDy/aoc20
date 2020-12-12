with open('input.txt', 'r') as f:
    data = f.read().splitlines()

    # I'm using the empty line ('') as the delimiter so
    # I have to manually add one at the end so the last
    # line won't get omitted.
    data.append('')

counts = list()
current_group_data = set()
for line in data:
    if line == '':
        counts.append(len(current_group_data))
        current_group_data = set()
    else:
        for question in line:
            current_group_data.add(question)

print(sum(counts))
