import config
import math

# return error message
def error(message):
    config.error = True
    return "Error: " + message

# solve operation
def solve(operation, depth = 0):
    # possible errors
    if operation == "":
        return error("operation is empty.")

    elif operation[-1] in config.OPERATORS:
        return error("ending with an operator.")
    
    elif operation[-1] == "(":
        return error("ending with an open parenthesis.")

    counter = 0
    for c in operation:
        counter += 1 if c == "(" else (-1 if c == ")" else 0)
    if counter != 0:
        return error("not all parentheses are closed.")

    def factorial(n, d=0):
        if n[-1] == "!":
            n = factorial(n[:-1], d+1)
            if n == "error":
                return n
            elif abs(round(n:=float(n)) - n) < 10 ** -7:
                n = round(n)
            else:
                return "error"
            r = 1
            for i in range(n):
                r *= i+1
            return r
        else:
            return n

    # transforming constants to floats
    done = False
    while not done:
        for i, c in enumerate(operation):
            if c == "π":
                operation = operation[:i] + config.pi + operation[i+1:]
                break
            elif c == "e" and (i == 0 or operation[i-1] not in config.NUMBERS):
                operation = operation[:i] + config.e + operation[i+1:]
                break
            if i == len(operation) - 1:
                done = True
    # transforming ln to log e
    while "ln" in operation:
        i = operation.index("ln")
        operation = operation[:i] + "log" + config.e + operation[i+2:]

    # solving logs
    def log(base, arg):
        return math.log(arg)/math.log(base) # change of base formula

    while "log" in operation:
        i = operation.index("log")
        for a, c in enumerate(operation[i:]):
            if c == "(":
                j = i + a + 1
        counter = 1
        for a, c in enumerate(operation[j:]):
            counter += 1 if c == "(" else (-1 if c == ")" else 0)
            if counter == 0:
                k = j + a
                break
        
        prefix = operation[:i]
        suffix = operation[k+1:]
        base = operation[i+3:j-1]
        arg = operation[j:k]
        try:
            operation = prefix + str(log(float(base), float(solve(arg, depth = depth+1)))) + suffix
        except ValueError:
                return error(f"invalid input for logarithm")
    
    # solving trig functions
    for func in sorted(config.trig, key = len)[::-1]: # sort by decresing length to first check for inverse functions
        if func in operation:
            i = operation.index(func)
            j = i + len(func) + 1

            counter = 1
            for a, c in enumerate(operation[j:]):
                counter += 1 if c == "(" else (-1 if c == ")" else 0)
                if counter == 0:
                    k = j + a
                    break

            prefix = operation[:i]
            suffix = operation[k+1:]
            try:
                operation = prefix + str(round(getattr(math, func)(float(solve(operation[j:k], depth+1))), 8)) + suffix
            except ValueError:
                return error(f"invalid input for {func}")

    # transforming roots to exponents
    while "√" in operation:
        for i, c in enumerate(operation):
            if c == "√":
                # find index
                # there is nothing to iterate through because the root is the first character
                if len(operation[:i]) == 0:
                    index = 2
                    prefix = ""
                # iterate through part of operation before the root (reversed)
                for j, d in enumerate(reversed(operation[:i])):
                    # there is a different character
                    if d not in config.NUMBERS + ".":
                        index = operation[i-j:i]
                        # the first character before the root is not a number
                        if index == "":
                            index = 2
                        prefix = operation[:i-j]
                        break
                    # all symbols were numbers
                    elif i-j == 1:
                        index = operation[:i]
                        prefix = ""
                
                # find expression
                counter = 0
                for j, d in enumerate(operation[i+1:]):
                    counter += 1 if d == "(" else (-1 if d == ")" else 0)
                    if counter == 0:
                        expression = operation[i+2:i+2+j-1]
                        suffix = operation[i+2+j:]
                        break

                # rewrite operation
                operation = f"{prefix}(({expression})^(1/{index})){suffix}"
                break
    
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
                                    return error("cannot take fractional exponent of negative numbers.")
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
                                return error("cannot take fractional exponent of negative numbers.")
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
            if operation[i-1] not in operators_pos and not (operation[i] == "+" and operation[i-1] == "e"): # minus sign after another sign
                operators.append(operation[i])
                operators_pos.append(i)
    l = list(operation)
    for i in operators_pos:
        l[i] = " "
    if l[0] == " ":
        l.insert(0, "0")
    l = "".join(l).split()
    operation = []
    for n in l:
        fac = factorial(n)
        if fac == "error":
            return error("cannot take factorial of non-integer.")
        else:
            operation += [str(float(fac))]

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

    operation = str(operation[0])

    if operation in ["inf", "-inf"]:
        return error("result too large")

    precision = 7
    rounding = 5
    if depth == 0:

        split_e = operation.split("e")
        operation = split_e[0]

        if "." in operation:
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
                operation = split_point[0] + "." + split_point[1][:rounding]

        if len(split_e) > 1:
            operation += "x10^" + split_e[1][1:]

    return operation
