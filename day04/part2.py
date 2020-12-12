import re


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


def validate_byr(value):
    if len(value) == 4:
        value = int(value)
        if 1920 <= value <= 2002:
            return True
    return False


def validate_iyr(value):
    if len(value) == 4:
        value = int(value)
        if 2010 <= value <= 2020:
            return True
    return False


def validate_eyr(value):
    if len(value) == 4:
        value = int(value)
        if 2020 <= value <= 2030:
            return True
    return False


def validate_hgt(value):
    match = re.match(r'^([\d]{3})cm|([\d]{2})in$', value)
    if match:
        centimeters, inches = match.groups()
        if centimeters is not None:
            if 150 <= int(centimeters) <= 193:
                return True
        elif inches is not None:
            if 59 <= int(inches) <= 76:
                return True
    return False


def validate_hcl(value):
    if re.match(r'^#[\da-f]{6}$', value):
        return True
    return False


def validate_ecl(value):
    if value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True
    return False


def validate_pid(value):
    if len(value) == 9:
        return True
    return False


def validate_cid(value):
    return True


REQUIRED_FIELDS = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid,
    'cid': validate_cid,
}

with open('input.txt', 'r') as fd:
    data = fd.read().splitlines()

    # I'm using the empty line ('') as the delimiter so
    # I have to manually add one at the end so the last
    # line won't get omitted.
    data.append('')

valid_passports = 0
for entry in parse_data(data):
    present_fields_keys = sorted(list(entry.keys()))

    if (
        sorted(REQUIRED_FIELDS.keys()) == present_fields_keys or
        sorted(REQUIRED_FIELDS.keys()) == sorted([*present_fields_keys, 'cid'])
    ):
        if all(REQUIRED_FIELDS[field](value) for field, value in entry.items()):
            valid_passports += 1

print(valid_passports)
