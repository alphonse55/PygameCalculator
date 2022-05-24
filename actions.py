from solve import solve, error
import config

def number(n):
    if config.solved:
        config.operations += [[str(n), ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    else:
        if len(config.operations[-1][0]) == 0 or config.operations[-1][0][-1] not in ")!eπ":
            config.operations[-1][0] += str(n)

def constant(n):
    if config.solved:
        config.operations += [[n, ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    else:
        if len(config.operations[-1][0]) == 0 or config.operations[-1][0][-1] in config.OPERATORS + list("("):
            config.operations[-1][0] += n

def canc():
    if config.solved:
        config.operations += [["", ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    else:
        config.operations[-1][0] = ""

def decimal_point():
    if not config.solved:
        last_decimal_point = -1
        sign_after_last_decimal_point = False
        for i in range(len(config.operations[-1][0])):
            if config.operations[-1][0][i] == ".":
                last_decimal_point = i
        if last_decimal_point == -1:
            sign_after_last_decimal_point = True
        else:
            for i in range(last_decimal_point, len(config.operations[-1][0])):
                if config.operations[-1][0][i] in config.OPERATORS + list("√"):
                    sign_after_last_decimal_point = True
        if sign_after_last_decimal_point and config.operations[-1][0] != "" and config.operations[-1][0][-1] in config.NUMBERS:
            config.operations[-1][0] += "."

def delete():
    if config.solved:
        config.operations += [[config.operations[config.operation_index][0][:-1], ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    else:
        config.operations[-1][0] = config.operations[-1][0][:-1]

def operator(sign):
    if config.solved:
        if not config.operations[config.operation_index][1].startswith("Error"):
            config.operations += [[config.operations[config.operation_index][1] + sign, ""]]
            config.operation_index = len(config.operations) - 1
            config.solved = False
    elif config.operations[-1][0] != "" and config.operations[-1][0][-1] in config.NUMBERS + ")!eπ":
        config.operations[-1][0] += sign

def power(sign):
    if config.solved:
        if not config.operations[config.operation_index][1].startswith("Error"):
            if "x" in config.operations[config.operation_index][1]:
                config.operations += [["(" + config.operations[config.operation_index][1] + ")" + sign, ""]]
            else:
                config.operations += [[config.operations[config.operation_index][1] + sign, ""]]
            config.operation_index = len(config.operations) - 1
            config.solved = False
    elif config.operations[-1][0] != "" and config.operations[-1][0][-1] in config.NUMBERS + ")!eπ":
        for i, c in enumerate(config.operations[-1][0][::-1]):
            if c in config.OPERATORS:
                if c == "^":
                    # temporary way to handle tower of exponents which basically blocks them by adding parentheses
                    for j, d in enumerate(config.operations[-1][0][-i-1::-1]):
                        if d in list(set(config.OPERATORS) - {"^"}):
                            cut = - i - j
                            break
                    else:
                        cut = 0
                    config.operations[-1][0] = config.operations[-1][0][:cut] + "(" + config.operations[-1][0][cut:] + ")^"
                    break
                else:
                    config.operations[-1][0] += sign
                    break
        else:
            config.operations[-1][0] += sign

def minus():
    if config.solved:
        if not config.operations[config.operation_index][1].startswith("Error"):
            config.operations += [[config.operations[config.operation_index][1] + "-", ""]]
        else:
            config.operations += [["-", ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    elif len(config.operations[-1][0]) == 0 or not (config.operations[-1][0][-1] in config.OPERATORS and (len(config.operations[-1][0]) > 1 and config.operations[-1][0][-2] in config.OPERATORS)):
        config.operations[-1][0] += "-"

def equals():
    if not config.solved:
        try:
            config.operations[-1][1] = solve(config.operations[-1][0])
        except OverflowError:
            config.operations[-1][1] = error("result too large.")
        config.solved = True

def ans():
    if not config.operations[-1][1].startswith("Error"):
        if config.solved:
            config.operations += [[config.operations[-1][1], ""]]
            config.operation_index = len(config.operations) - 1
            config.solved = False
        elif len(config.operations[-1][0]) == 0 or config.operations[-1][0][-1] in config.OPERATORS + list("("):
            results = [o[1] for o in reversed(config.operations[:-1])]
            for result in results:
                if not result.startswith("Error"):
                    config.operations[-1][0] += result
                    break

def other():
    if config.buttons == config.first_page:
        config.other.text = "1st"
        config.buttons = config.second_page
    else:
        config.other.text = "2nd"
        config.buttons = config.first_page

def left():
    for last_bracket, c in enumerate(config.operations[-1][0][::-1]):
        if c == "(":
            last_bracket = len(config.operations[-1][0][::-1]) - last_bracket - 1
            break
    else:
        last_bracket = -1
        
    if config.solved:
        config.operations += [["(", ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    elif (len(config.operations[-1][0]) == 0) or (config.operations[-1][0][-1] in config.OPERATORS + list("(")) or (("log" in config.operations[-1][0]) and (config.operations[-1][0][-1] in config.NUMBERS) and (last_bracket < config.operations[-1][0].index("log"))):
        config.operations[-1][0] += "("

def right():
    counter = 0
    if not config.solved:
        for c in config.operations[-1][0]:
            counter += 1 if c == "(" else (-1 if c == ")" else 0)
        if counter > 0 and config.operations[-1][0][-1] not in config.OPERATORS + list("("):
            config.operations[-1][0] += ")"

def back():
    config.operation_index -= 1

def next():
    config.operation_index += 1

def root(n):
    if config.solved:
        config.operations += [[f"{n if n>2 else ''}√(", ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    elif len(config.operations[-1][0]) == 0 or config.operations[-1][0][-1] in config.OPERATORS + list("("):
        config.operations[-1][0] += f"{n if n>2 else ''}√("

# def root3():
#     if config.solved:
#         config.operations += [["3√(", ""]]
#         config.operation_index = len(config.operations) - 1
#         config.solved = False
#     elif len(config.operations[-1][0]) == 0 or config.operations[-1][0][-1] in config.OPERATORS + list("("):
#         config.operations[-1][0] += "3√("

def rooty():
    if not config.solved:
        if config.operations[-1][0] != "" and config.operations[-1][0][-1] in config.NUMBERS:
                config.operations[-1][0] += "√("

def factorial():
    if config.operations[-1][0] != "" and config.operations[-1][0][-1] in config.NUMBERS + ")!eπ":
        if config.solved:
            config.operations += [[config.operations[-1][0] + "!", ""]]
            config.operation_index = len(config.operations) - 1
            config.solved = False
        else:
            config.operations[-1][0] += "!"

def power_10():
    if config.operations[-1][0] != "" and config.operations[-1][0][-1] in config.NUMBERS + ")!eπ":
        if config.solved:
            config.operations += [[config.operations[-1][0] + "x10^", ""]]
            config.operation_index = len(config.operations) - 1
            config.solved = False
        else:
            config.operations[-1][0] += "x10^"

def func(func):
    if func == "logy":
        func = "log"
    else:
        func += "("

    if config.solved:
        config.operations += [[func, ""]]
        config.operation_index = len(config.operations) - 1
        config.solved = False
    else:
        if len(config.operations[-1][0]) == 0 or config.operations[-1][0][-1] in config.OPERATORS + list("("):
            config.operations[-1][0] += func