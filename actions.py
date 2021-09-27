from solve import solve
import config

operation_is_result = False

def number(operation, last_operation, result, n):
    if len(operation) == 0 or operation[-1] != ")":
        global operation_is_result
        if operation_is_result:
            operation = str(n)
            last_operation += result
            operation_is_result = False
        else:
            operation += str(n)
    return operation, last_operation, result

def constant(operation, last_operation, result, n):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += str(n)
    return operation, last_operation, result

def canc(operation, last_operation, result):
    global operation_is_result
    operation_is_result = False
    return "", "", result

def decimal_point(operation, last_operation, result):
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
    if not operation_is_result and sign_after_last_decimal_point and operation != "" and operation[-1] in config.NUMBERS:
        operation += "."
    return operation, last_operation, result

def delete(operation, last_operation, result):
    if not operation_is_result:
        operation = operation[:-1]
    return operation, last_operation, result

def sign(operation, last_operation, result, sign):
    if operation != "" and operation[-1] in config.NUMBERS + ")":
        operation += sign
        global operation_is_result
        if operation_is_result:
            last_operation += result
            operation_is_result = False
    return operation, last_operation, result

def minus(operation, last_operation, result):
    if len(operation) == 0 or not (operation[-1] in config.OPERATORS and operation[-2] in config.OPERATORS):
        operation += "-"        
        global operation_is_result
        if operation_is_result:
            last_operation += result
            operation_is_result = False
    return operation, last_operation, result

def equals(operation, last_operation, result):
    result = solve(operation)
    last_operation = operation
    operation = result
    if not config.error:
        last_operation += " = "
        global operation_is_result
        operation_is_result = True
    return operation, last_operation, result

def ans(operation, last_operation, result):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += str(result)
    return operation, last_operation, result

def other(operation, last_operation, result):
    return operation, last_operation, result

def left(operation, last_operation, result):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += "("
    global operation_is_result
    if operation_is_result:
        operation = "("
        last_operation += result
        operation_is_result = False
    return operation, last_operation, result

def right(operation, last_operation, result):
    counter = 0
    for c in operation:
        counter += 1 if c == "(" else (-1 if c == ")" else 0)
    if counter > 0 and operation[-1] not in config.OPERATORS + ["("]:
        operation += ")"
    return operation, last_operation, result

def func(operation, last_operation, result, name):
    if len(operation) == 0 or operation[-1] in config.OPERATORS + ["("]:
        operation += name + "("
    return operation, last_operation, result

def back(operation, last_operation, result):
    config.error = False
    config.operation_font = config.font[60]
    return last_operation, "", result