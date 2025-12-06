
def calculate(numbers, operators):

    results = [0 for i in range(len(operators))]

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


numbers = []
operators = []

with open("6/input.txt", "r") as file:

    lines = file.readlines()

    for line_index, line in enumerate(lines):
        if line_index == len(lines)-1:
            operators = line.rstrip().split()
            break

        numbers.append(
            line.rstrip().split()
        )

print(
    calculate(numbers, operators)
)


