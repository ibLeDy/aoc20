def is_letter_in_correct_position(password, letter, position):
    try:
        if password[position - 1] == letter:
            return True
    except IndexError:
        pass
    return False


with open('input.txt', 'r') as fd:
    data = fd.read().splitlines()

valid_passwords = 0
for entry in data:
    positions, letter, password = entry.split(' ')

    position1, position2 = map(int, positions.split('-'))
    letter = letter.strip(':')

    letters_in_correct_position = 0
    if is_letter_in_correct_position(password, letter, position1):
        letters_in_correct_position += 1
    if is_letter_in_correct_position(password, letter, position2):
        letters_in_correct_position += 1

    if letters_in_correct_position == 1:
        valid_passwords += 1

print(valid_passwords)
