from z3 import Int, Solver, sat

def calc(buttons, results):
    z_buttons = [
        Int(f"b{i}") for i in range(len(buttons))
    ]

    button_constraints_dict = {}
    for i, button in enumerate(buttons):
        for wire in button:
            
            if wire in button_constraints_dict:
                button_constraints_dict[wire] += z_buttons[i]

            else:
                button_constraints_dict[wire] = z_buttons[i]

    button_constraints = [
        results[k] == button_constraints_dict[k] for k in button_constraints_dict
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
    
buttons = [
    (0,2),
    (0,),
    (1,),
    (2,)
]
result = (2,1,2)

print(
    calc(buttons, result)
)
