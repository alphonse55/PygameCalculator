import config

def solve(operation, depth = 0):
    # return error message
    def error(message):
        config.error = True
        return "Error: " + message

    # possible errors
    if operation == "":
        return error("operation is empty")

    elif operation[-1] in config.OPERATORS:
        return error("ending with an operator")
    
    elif operation[-1] == "(":
        return error("ending with an open parenthesis")

    counter = 0
    for c in operation:
        counter += 1 if c == "(" else (-1 if c == ")" else 0)
    if counter != 0:
        return error("not all parentheses are closed")

    # transforming roots to exponents
    radicals = True
    while radicals:
        for i, c in enumerate(operation):
            if c == "√":
                # find index
                for j, d in enumerate(operation[:i-1:-1]):
                    if d not in config.NUMBERS + ".":
                        index = operation[j+1:i]
                        break
                # find expression
                counter = 0
                for k, e in enumerate(operation[i+1:]):
                    counter += 1 if e == "(" else (-1 if e == ")" else 0)
                    if counter == 0:
                        expression = operation[i+2:i+2+k-1]
                        break
                
                prefix = operation[:j+1]
                suffix = operation[i+2+k:]

                operation = f"{prefix}({expression})^(1/{index}){suffix}"
            if i == len(operation) - 1:
                radicals = False

    # handling parentheses
    for i in range(len(operation)):
        if operation[i] == "(":
            counter = 1
            for j in range(i+1, len(operation)):
                counter += 1 if operation[j] == "(" else (-1 if operation[j] == ")" else 0)
                if counter == 0:
                    break
            
            solved_brackets = solve(operation[i+1:j], depth+1)

            # handling negative bases in parentheses
            if float(solved_brackets) < 0:
                if j < len(operation) - 1:
                    if operation[j+1] == "^":
                        #finding exponent
                        ind = j+2
                        exponent = ""
                        if operation[ind] in config.NUMBERS:
                            while True:
                                if operation[ind] in config.NUMBERS:
                                    exponent += operation[ind]
                                elif operation[ind] == ".":
                                    return error("cannot take fractional exponent of negative numbers")
                                else:
                                    break

                                if ind < len(operation) - 1:
                                    ind += 1
                                else:
                                    break
                            exponent = int(exponent)

                        elif operation[ind] == "(":
                            counter = 0
                            for k, char in enumerate(operation[ind:]):
                                counter += 1 if char == "(" else (-1 if char == ")" else 0)
                                if counter == 0:
                                    break
                            exponent = solve(operation[ind+1:ind+k])
                            if "." in exponent:
                                return error("cannot take fractional exponent of negative numbers")
                            else:
                                exponent = int(exponent)

                        # inverting result if needed
                        if exponent % 2 == 0:
                            solved_brackets = str(-float(solved_brackets))
            
            return solve(operation[:i] + solved_brackets + operation[j+1:], depth)

    operators = []
    operators_pos = []
    to_pop = []

    for i in range(len(operation)):
        if operation[i] in config.OPERATORS:
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

    for i in range(len(operators)):
        if operators[i] == "^":
            base = float(operation[i - len(to_pop)])
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
            operation[i - len(to_pop)] = float(operation[i - len(to_pop)]) * float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)
        elif operators[i] == "/":
            operation[i - len(to_pop)] = float(operation[i - len(to_pop)]) / float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    i = len(to_pop) - 1
    while i >= 0:
        operators.pop(to_pop[i])
        i -= 1

    to_pop = []

    for i in range(len(operators)):
        if operators[i] == "+":
            operation[i - len(to_pop)] = float(operation[i - len(to_pop)]) + float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)
        elif operators[i] == "-":
            operation[i - len(to_pop)] = float(operation[i - len(to_pop)]) - float(operation[i + 1 - len(to_pop)])
            operation.pop(i + 1 - len(to_pop))
            to_pop.append(i)
    
    split_e = str(operation[0]).split("e")
    operation = split_e[0]

    # do rounding only for the first call of solve(), with depth = 0
    precision = 5
    if depth == 0 and "." in operation:
        split_point = operation.split(".")
        for i in range(len(split_point[1])):
            if split_point[1][i:i + precision] == "0" * precision:
                if i == 0:
                    split_point[1] = "0"
                else:
                    split_point[1] = split_point[1][:i]
                break
            elif split_point[1][i:i + precision] == "9" * precision:
                if i == 0:
                    split_point[0] = str(int(split_point[0]) + 1)
                    split_point[1] = "0"
                else:
                    split_point[1] = str(int(split_point[1][:i]) + 1)
                break

        if split_point[1] == "0":
            operation = split_point[0]
        else:
            operation = split_point[0] + "." + split_point[1][:4]

    if len(split_e) > 1:
        operation += "x10^" + split_e[1][1:]
    
    return operation
