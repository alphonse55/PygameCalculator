def solve(operation, OPERATORS):
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

    operation = str(operation[0])
    if operation[-2:] == ".0":
        operation = operation[0:-2]
    split = operation.split("e")
    if len(split) == 1:
        operation = split[0]
    else:
        operation = split[0] + "x10^" + split[1][1:]
    return operation