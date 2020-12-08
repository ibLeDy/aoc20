def get_three_entries(data):
    for entry1 in data:
        for entry2 in data:
            difference = 2020 - (entry1 + entry2)
            if difference in data:
                print(entry1 * entry2 * difference)
                return


with open('input.txt', 'r') as fp:
    data = set(map(int, fp.read().splitlines()))
    get_three_entries(data)
