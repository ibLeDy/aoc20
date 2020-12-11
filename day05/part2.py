TOTAL_ROWS = 128
TOTAL_COLUMNS = 8
TOTAL_SEATS = TOTAL_ROWS * TOTAL_COLUMNS


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


def get_my_seat(missing_seats):
    for seat in missing_seats:
        if seat + 1 in seat_ids and seat - 1 in seat_ids:
            return seat


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

seat_ids = set()
for instructions in data:
    seat_ids.add(get_seat_id(get_row(instructions[:7]), get_column(instructions[7:])))

print(get_my_seat([num for num in range(TOTAL_SEATS) if num not in seat_ids]))
