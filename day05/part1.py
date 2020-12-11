TOTAL_ROWS = 128
TOTAL_COLUMNS = 8


def get_row(instructions):
    current_row = list(range(TOTAL_ROWS))
    for row in instructions:
        if row == 'F':
            current_row = current_row[:len(current_row) // 2]
        elif row == 'B':
            current_row = current_row[len(current_row) // 2:]
    return current_row[0]


def get_column(instructions):
    current_column = list(range(TOTAL_COLUMNS))
    for column in instructions:
        if column == 'L':
            current_column = current_column[:len(current_column) // 2]
        elif column == 'R':
            current_column = current_column[len(current_column) // 2:]
    return current_column[0]


def get_seat_id(row, column):
    return (row * 8) + column


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

seat_ids = set()
for instructions in data:
    seat_ids.add(get_seat_id(get_row(instructions[:7]), get_column(instructions[7:])))

print(max(seat_ids))
