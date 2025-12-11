import math
import sys
import time

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

    def set_joltage(self): # too slow
        start_joltage = tuple([0 for _ in range(len(self.joltage_requirements))])
        combinations = set()
        combinations.add(start_joltage)

        i = 1
        while True:
            new_combinations = set()

            for combination in combinations:
                list_combination = list(combination)

                for button in self.buttons:

                    combination_cp = list_combination.copy()

                    for wire in button:
                        combination_cp[wire] += 1

                    equal = True
                    too_high = False
                    for j, v in enumerate(combination_cp):

                        if v > self.joltage_requirements[j]:
                            too_high = True
                            break

                        if v != self.joltage_requirements[j]:
                            equal = False

                    if too_high:
                        continue

                    if equal:
                        return i

                    new_combinations.add(
                        tuple(combination_cp)
                    )

            combinations = new_combinations.copy()
            i += 1

class Node():
    def __init__(self, values, goal, buttons, cost):
        self.cost = cost
        self.values = values
        self.goal = goal
        self.buttons = buttons

        self.heuristic = self.calculate_distance(goal)
        self.estimated = self.cost + self.heuristic
    
    def calculate_distance(self, other_values):
        a = self.values
        b = other_values

        subtracted = [v - b[i] for i, v in enumerate(a)]
        squared = [i ** 2 for i in subtracted]

        added = 0
        for num in squared:
            added += num

        return math.sqrt(added)
    
    def is_over_goal(self):
        for i, part in enumerate(self.values):
            if part > self.goal[i]:
                return True
            
        return False
    
    def discover(self):
        global discovered_nodes
        #print(self.is_over_goal(), self.heuristic, self.values)

        if self.is_over_goal():
            return None

        if self.values in discovered_nodes:
            return None
        
        discovered_nodes.append(self.values)

        #if self.values in self.already_found:
        #    return False, self.already_found

        if self.heuristic == 0:
            return 0#, self.already_found
        
        options = []
        for button in self.buttons:
            
            values_cp = self.values.copy()

            for wire in button:
                values_cp[wire] += 1

            new_cost = self.cost + self.calculate_distance(values_cp)

            options.append(
                Node(values_cp.copy(), self.goal, self.buttons, new_cost)
            )

        for node in sorted(options):
            res = node.discover()
            if res is not None:
                return res + 1#, self.already_found
            
        return None

    def __repr__(self):
        return self.estimated
    
    def __lt__(self, other):
        return self.estimated < other.estimated
    
    def __gt__(self, other):
        return self.estimated > other.estimated

def p1(machines):

    total = 0
    for machine in machines:
        total += machine.set_indicator_lights()

    return total

def p2(machines):

    print("--------------------------")

    total = 0
    for i, machine in enumerate(machines):
        print(f"{(i/len(machines))*100:.2f}%")
        total += machine.set_joltage()

    print("--------------------------")

    return total

def p2_astar(machines):

    total = 0

    for machine in machines:
        start = [0 for _ in range(len(machine.joltage_requirements))]
        start_node = Node(start, machine.joltage_requirements, machine.buttons, 0)

        v = start_node.discover()
        print(f"+ {v}")

        total += v

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

#print(
#    p2(machines)
#)

sys.setrecursionlimit(10000000)

discovered_nodes = []

s = time.perf_counter()
print(
    p2_astar(machines)
)
e = time.perf_counter()

print(f"time: {(e-s)*1000:.2f}ms")
