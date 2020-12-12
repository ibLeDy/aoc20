def parse_data(data):
    parsed_entries = []
    current_fields = {}
    for entry in data:
        if entry:
            for field in entry.split(' '):
                key, value = field.split(':')
                current_fields[key] = value
        else:
            parsed_entries.append(current_fields)
            current_fields = {}

    return parsed_entries


REQUIRED_FIELDS = sorted([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
])

with open('input.txt', 'r') as fd:
    data = fd.read().splitlines()

    # I'm using the empty line ('') as the delimiter so
    # I have to manually add one at the end so the last
    # line won't get omitted.
    data.append('')

valid_passports = 0
for entry in parse_data(data):
    present_fields = sorted(list(entry.keys()))

    if REQUIRED_FIELDS == present_fields:
        valid_passports += 1
    elif REQUIRED_FIELDS == sorted([*present_fields, 'cid']):
        valid_passports += 1

print(valid_passports)
