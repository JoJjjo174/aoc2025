from z3 import Int, Solver, sat

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
            combinations = new_combinations

    def set_joltage(self):
        z_buttons = [
            Int(f"b{i}") for i in range(len(self.buttons))
        ]

        button_constraints_dict = {}
        for i, button in enumerate(self.buttons):
            for wire in button:
                
                if wire in button_constraints_dict:
                    button_constraints_dict[wire] += z_buttons[i]

                else:
                    button_constraints_dict[wire] = z_buttons[i]

        button_constraints = [
            self.joltage_requirements[k] == button_constraints_dict[k] for k in button_constraints_dict
        ]

        total = Int("t")
        total_parts = None

        for z_button in z_buttons:
            if total_parts is not None:
                total_parts += z_button

            else:
                total_parts = z_button

        total_constraint = [
            total == total_parts
        ]

        above_zero_constraints = [
            i >= 0 for i in z_buttons
        ]

        s = Solver()

        s.add(button_constraints)
        s.add(total_constraint)
        s.add(above_zero_constraints)

        all_solutions = []

        while s.check() == sat:
            model = s.model()
            sol = model[total].as_long()
            all_solutions.append(sol)

            s.add(
                total != sol
            )

        return min(all_solutions)

def p1(machines):

    total = 0
    for machine in machines:
        total += machine.set_indicator_lights()

    return total

def p2(machines):

    total = 0
    for machine in machines:
        total += machine.set_joltage()

    return total

machines = []
with open("10/input.txt", "r") as file:
    for line in file.readlines():
        split_line = line.rstrip().split()

        indicator_lights = split_line[0][1:-1]
        buttons = split_line[1:-1]
        joltage_requirements = split_line[-1][1:-1].split(",")

        machines.append(
            Machine(indicator_lights, [[int(i) for i in b[1:-1].split(",")] for b in buttons], [int(i) for i in joltage_requirements])
        )

print(
    p1(machines)
)

print(
    p2(machines)
)
