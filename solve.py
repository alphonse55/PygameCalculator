OPERATORS = ["+", "-", "x", "/", "^"]

def solve(operation, depth = 0):
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
            return solve(operation[:i] + solve(operation[i+1:j], depth+1) + operation[j+1:], depth)

    operators = []
    operators_pos = []
    to_pop = []

    for i in range(len(operation)):
        if operation[i] in OPERATORS:
            if i-1 not in operators_pos: # minus sign after another sign
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
            base = operation[i - len(to_pop)]
            minus_before_base = False
            if str(operation[i - len(to_pop)])[0] == "-":
                minus_before_base = True
                base *= -1
            operation[i - len(to_pop)] = base ** float(operation[i + 1 - len(to_pop)])
            if minus_before_base:
                operation[i - len(to_pop)] *= -1
            
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

    # do rounding only if there are no brackets, so it is the last time solve() is executed
    if depth == 0:
        split_point = operation.split(".")
        if int(split_point[1][:4]) == 0:
            operation = split_point[0]
        else:
            operation = split_point[0] + "." + split_point[1][:4]

    if len(split_e) > 1:
        operation += "x10^" + split_e[1][1:]
    
    print(operation)
    return operation