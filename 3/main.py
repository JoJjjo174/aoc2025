
def get_highest_joltage(bank):
    max_digit, position = find_highest_value(bank[:-1])

    string2 = bank[position+1:]
    max_digit_2, _ = find_highest_value(string2)

    max_joltage = str(max_digit) + str(max_digit_2)

    return int(max_joltage)

def get_highest_joltage_2(bank, digits = 12):

    current_joltage = ""
    position = -1

    for i in range(digits):
        cut_at_end = (digits-i-1)
        if cut_at_end != 0:
            string = bank[position+1:-cut_at_end]

        else:
            string = bank[position+1:]

        max_digit, position2 = find_highest_value(string)

        current_joltage += str(max_digit)
        position = position + position2 + 1

    return int(current_joltage)

def find_highest_value(string):
    max_digit = 0
    position = 0


    for index in range(len(string)):
        char = string[index]

        if int(char) > max_digit:
            max_digit = int(char)
            position = index

    return max_digit, position

total_value = 0
total_value_2 = 0

with open("3/input.txt", "r") as file:
    for line in file.readlines():
        bank = line.rstrip()
        total_value += get_highest_joltage(bank)
        total_value_2 += get_highest_joltage_2(bank)

print(
    total_value
)
print(
    total_value_2
)



