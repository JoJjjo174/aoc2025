
class Machine():
    def __init__(self, required_indicator_lights, buttons, joltage_requirements):
        self.required_indicator_lights = required_indicator_lights
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements

    def set_indicator_lights(self):
        off_indicator_lights = "." * len(self.required_indicator_lights)
        combinations = set()
        combinations.add(off_indicator_lights)

        i = 1
        while True:

            new_combinations = set()

            for combination in combinations:
                for button in self.buttons:

                    list_combination = list(combination)

                    for toggle in button:
                        list_combination[int(toggle)] = "#" if list_combination[int(toggle)] == "." else "."

                    str_combination = "".join(list_combination)

                    if str_combination == self.required_indicator_lights:
                        return i

                    new_combinations.add(str_combination)

            i += 1
            combinations = new_combinations.copy()

def p1(machines):

    total = 0
    for machine in machines:
        total += machine.set_indicator_lights()

    return total

machines = []
with open("10/input.txt", "r") as file:
    for line in file.readlines():
        split_line = line.rstrip().split()

        indicator_lights = split_line[0][1:-1]
        buttons = split_line[1:-1]
        joltage_requirements = split_line[-1]

        machines.append(
            Machine(indicator_lights, [b[1:-1].split(",") for b in buttons], joltage_requirements)
        )
        
print(
    p1(machines)
)