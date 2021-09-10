def solve(operation, OPERATORS):
    # print(operation)
    for i in range(len(operation)):
        if operation[i] == "(":
            left_counter = 1
            right_counter = 0
            for j in range(i+1, len(operation)):
                if operation[j] == "(":
                    left_counter += 1
                elif operation[j] == ")":
                    right_counter += 1
                    if right_counter == left_counter:
                        break
            print(operation[:i])
            print(operation[i+1:j])
            print(operation[j+1:])
            # print(solve(operation[:i] + solve(operation[i+1:j], OPERATORS) + operation[j+1:], OPERATORS))
            return solve(operation[:i] + solve(operation[i+1:j], OPERATORS) + operation[j+1:], OPERATORS)
    operators = []
    operators_pos = []
    to_pop = []
    for i in range(len(operation)):
        if operation[i] in OPERATORS:
            operators.append(operation[i])
            operators_pos.append(i)
    list1 = list(operation)
    for i in operators_pos:
        list1[i] = " "
    if list1[0] == " ":
        list1.insert(0, "0")
    operation = "".join(list1)
    operation = operation.split()
    for i in range(len(operation)):
        operation[i] = float(operation[i])

    for i in range(len(operators)):
        if operators[i] == "^":
            operation[i - len(to_pop)] **= float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    i = len(to_pop) - 1
    while i >= 0:
        operators.pop(to_pop[i])
        i -= 1

    to_pop = []

    for i in range(len(operators)):
        if operators[i] == "x":
            operation[i - len(to_pop)] *= float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)
        elif operators[i] == "/":
            operation[i - len(to_pop)] /= float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    i = len(to_pop) - 1
    while i >= 0:
        operators.pop(to_pop[i])
        i -= 1

    to_pop = []

    for i in range(len(operators)):
        if operators[i] == "+":
            operation[i - len(to_pop)] += float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)
        elif operators[i] == "-":
            operation[i - len(to_pop)] -= float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    split_e = str(operation[0]).split("e")
    operation = split_e[0]

    if len(split_point := operation.split(".")) > 1:
        operation = split_point[0] + "." + split_point[1][:4]

    if len(split_e) > 1:
        operation += "x10^" + split_e[1][1:]

    return operation