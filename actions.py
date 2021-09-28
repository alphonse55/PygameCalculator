from solve import solve
import config

operation_is_result = False

def number(operation, result, n):
    if len(operation) == 0 or operation[-1] != ")":
        operation += str(n)
    return operation, result

def constant(operation, result, n):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += str(n)
    return operation, result

def canc(operation, result):
    return "", result

def decimal_point(operation, result):
    last_decimal_point = -1
    sign_after_last_decimal_point = False
    for i in range(len(operation)):
        if operation[i] == ".":
            last_decimal_point = i
    if last_decimal_point == -1:
        sign_after_last_decimal_point = True
    else:
        for i in range(last_decimal_point, len(operation)):
            if operation[i] in config.OPERATORS:
                sign_after_last_decimal_point = True
    if sign_after_last_decimal_point and operation != "" and operation[-1] in config.NUMBERS:
        operation += "."
    return operation, result

def delete(operation, result):
    if not operation_is_result:
        operation = operation[:-1]
    return operation, result

def sign(operation, result, sign):
    if operation != "" and operation[-1] in config.NUMBERS + ")":
        operation += sign
    return operation, result

def minus(operation, result):
    if len(operation) == 0 or not (operation[-1] in config.OPERATORS and operation[-2] in config.OPERATORS):
        operation += "-"
    return operation, result

def equals(operation, result):
    result = solve(operation)
    config.operations += [[operation, result]]
    config.operation_index = len(config.operations) - 1
    config.solved = True
    print(config.operations, config.operation_index)
    return operation, result

def ans(operation, result):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += str(result)
    return operation, result

def other(operation, result):
    if config.buttons == config.first_page:
        config.other.text = "1st"
        config.buttons = config.second_page
    else:
        config.other.text = "2nd"
        config.buttons = config.first_page
    return operation, result

def left(operation, result):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += "("
    return operation, result

def right(operation, result):
    counter = 0
    for c in operation:
        counter += 1 if c == "(" else (-1 if c == ")" else 0)
    if counter > 0 and operation[-1] not in config.OPERATORS + ["("]:
        operation += ")"
    return operation, result

def func(operation, result, name):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += name + "("
    return operation, result

def back(operation, result):
    if config.operation_index > 0:
        if config.error:
            config.error = False
        config.operation_index -= 1
        stored_operation = config.operations[config.operation_index]
        print(config.operations, config.operation_index)
        return stored_operation[0], stored_operation[1]
    else:
        return operation, result

def next(operation, result):
    if config.operation_index < len(config.operations) - 1:
        if config.error:
            config.error = False
        config.operation_index += 1
        stored_operation = config.operations[config.operation_index]
        print(config.operations, config.operation_index)
        return stored_operation[0], stored_operation[1]
    else:
        return operation, result
