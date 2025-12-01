import math

def solve(turns):

    dial = 50
    zero_counts = 0


    for turn in turns:
        direction = -1 if turn[0] == "L" else 1
        amount = int(turn[1:])

        dial += direction * amount

        dial = dial % 100

        if dial == 0:
            zero_counts += 1

    return zero_counts

def solve_2(turns):
    dial = 50
    zero_counts = 0


    for turn in turns:
        direction = turn[0] == "R"
        amount = int(turn[1:])

        for i in range(amount):
            result = click(dial, direction)

            zero_counts += result[0]
            dial = result[1]

    return zero_counts

def click(dial: int, pos: bool):

    add = 1 if pos else -1
    dial += add
    dial = dial % 100

    if dial == 0:
        return 1, dial
    
    return 0, dial
    


def mod_count_zeroes():
    pass

inputs = []

with open("1/input.txt", "r") as file:
    for line in file.readlines():
        inputs.append(line.rstrip())

print(
    solve(inputs)
)

print(
    solve_2(inputs)
)
