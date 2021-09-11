from solve import solve

NUMBERS = '1234567890'
OPERATORS = ["+", "-", "x", "/", "^"]

def number(operation, last_operation, answer, n):
    if len(operation) == 0 or operation[-1] != ")":
        operation += str(n)
    return operation, last_operation, answer

def constant(operation, last_operation, answer, n):
    if len(operation) == 0 or operation[-1] in OPERATORS + ["("]:
        operation += str(n)
    return operation, last_operation, answer

def canc(operation, last_operation, answer):
    return "", "", answer

def decimal_point(operation, last_operation, answer):
    sign = False
    last_decimal_point = -1
    for i in range(len(operation)):
        if operation[i] == ".":
            last_decimal_point = i
    if last_decimal_point == -1:
        sign = True
    else:
        for i in range(last_decimal_point, len(operation)):
            if operation[i] in OPERATORS:
                sign = True
    if operation != "" and operation[-1] in NUMBERS and sign:
        operation += "."
    return operation, last_operation, answer

def delete(operation, last_operation, answer):
    return operation[:-1], last_operation, answer

def sign(operation, last_operation, answer, sign):
    if operation != "" and operation[-1] in NUMBERS + ")":
        operation += sign
    return operation, last_operation, answer

def equals(operation, last_operation, answer):
    try:
        answer = solve(operation, OPERATORS)
        last_operation = operation + "=" + answer
        operation = ""
    finally:
        return operation, last_operation, answer

def ans(operation, last_operation, answer):
    if len(operation) == 0 or operation[-1] in OPERATORS + ["("]:
        operation += str(answer)
    return operation, last_operation, answer

def other(operation, last_operation, answer):
    return operation, last_operation, answer

def left(operation, last_operation, answer):
    if len(operation) == 0 or operation[-1] in OPERATORS + ["("]:
        operation += "("
    return operation, last_operation, answer

def right(operation, last_operation, answer):
    counter = 0
    for c in operation:
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
    if counter > 0 and operation[-1] not in OPERATORS + ["("]:
        operation += ")"
    return operation, last_operation, answer

def func(operation, last_operation, answer, name):
    if len(operation) == 0 or operation[-1] in OPERATORS:
        operation += name + "("
    return operation, last_operation, answer