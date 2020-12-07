with open('input.txt', 'r') as fd:
    data = fd.read().splitlines()

valid_passwords = 0
for entry in data:
    amount, letter, password = entry.split(' ')

    amount_min, amount_max = map(int, amount.split('-'))
    letter = letter.strip(':')

    actual_amount = password.count(letter)
    if actual_amount >= amount_min and actual_amount <= amount_max:
        valid_passwords += 1

print(valid_passwords)
