
def calculate(numbers, operators):

    results = [0 for _ in range(len(operators))]

    for column in range(len(operators)):

        operator = operators[column]

        for row in range(len(numbers)):

            match operator:
                case "+":
                    results[column] += int(numbers[row][column])

                case "*":
                    if results[column] == 0:
                        results[column] = 1

                    results[column] *= int(numbers[row][column])

    return sum(results)

def calculate_p2(numbers, operators):
    
    results = [0 for _ in range(len(operators))]

    for big_column_index in range(len(operators)):
        big_column = get_big_column(numbers, big_column_index)
        numbers_calc = parse_big_column_numbers(big_column)

        match operators[big_column_index]:
            case "+":
                for num in numbers_calc:
                    results[big_column_index] += num

            case "*":
                if results[big_column_index] == 0:
                    results[big_column_index] = 1

                for num in numbers_calc:
                    results[big_column_index] *= num

    return sum(results)

def parse_big_column_numbers(big_column):
    numbers = ["" for _ in range(len(big_column[0]))]

    for row in big_column:
        for i in range(len(big_column[0])):
            small_column = row[i]
            if small_column == " ":
                continue

            numbers[i] = numbers[i] + small_column

    int_numbers = [int(i) for i in numbers[:-1]]
    return int_numbers

def get_big_column(numbers, column):
    big_column = []

    for row in numbers:
        big_column.append(
            row[column]
        )

    return big_column

numbers = []
operators_raw = []
operators = []
numbers_p2 = []

with open("6/input.txt", "r") as file:

    lines = file.readlines()

    for line_index, line in enumerate(lines):
        if line_index == len(lines)-1:
            operators_raw = line.rstrip()
            operators = line.rstrip().split()
            break

        numbers.append(
            line.rstrip().split()
        )

    for line in lines:
        if "+" in line or "*" in line:
            break

        line_cp = line[:-1] + " "

        split_line = []

        old_index = 0
        for index, char in enumerate(operators_raw):
            if char != " " and index != 0:
                split_line.append(
                    line_cp[old_index:index]
                )
                old_index = index

        split_line.append(line_cp[old_index:])

        numbers_p2.append(split_line)

print(
    calculate(numbers, operators)
)

print(
    calculate_p2(numbers_p2, operators)
)


