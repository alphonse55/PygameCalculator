from solve import solve

NUMBERS = '1234567890'
OPERATORS = ["+", "-", "x", "/", "^"]
operation_is_answer = False

def number(operation, last_operation, answer, n):
    if len(operation) == 0 or operation[-1] != ")":
        global operation_is_answer
        if operation_is_answer:
            operation = str(n)
            last_operation += answer
            operation_is_answer = False
        else:
            operation += str(n)
    return operation, last_operation, answer

def constant(operation, last_operation, answer, n):
    if len(operation) == 0 or operation[-1] in OPERATORS + ["("]:
        operation += str(n)
    return operation, last_operation, answer

def canc(operation, last_operation, answer):
    global operation_is_answer
    operation_is_answer = False
    return "", "", answer

def decimal_point(operation, last_operation, answer):
    last_decimal_point = -1
    sign_after_last_decimal_point = False
    for i in range(len(operation)):
        if operation[i] == ".":
            last_decimal_point = i
    if last_decimal_point == -1:
        sign_after_last_decimal_point = True
    else:
        for i in range(last_decimal_point, len(operation)):
            if operation[i] in OPERATORS:
                sign_after_last_decimal_point = True
    if not operation_is_answer and sign_after_last_decimal_point and operation != "" and operation[-1] in NUMBERS:
        operation += "."
    return operation, last_operation, answer

def delete(operation, last_operation, answer):
    if not operation_is_answer:
        operation = operation[:-1]
    return operation, last_operation, answer

def sign(operation, last_operation, answer, sign):
    if operation != "" and operation[-1] in NUMBERS + ")":
        operation += sign
        global operation_is_answer
        if operation_is_answer:
            last_operation += answer
            operation_is_answer = False
    return operation, last_operation, answer

def minus(operation, last_operation, answer):
    if len(operation) == 0 or not (operation[-1] in OPERATORS and operation[-2] in OPERATORS):
        operation += "-"        
        global operation_is_answer
        if operation_is_answer:
            last_operation += answer
            operation_is_answer = False
    return operation, last_operation, answer

def equals(operation, last_operation, answer):
    try:
        answer = solve(operation)
        last_operation = operation + "="
        operation = answer
        global operation_is_answer
        operation_is_answer = True
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
        counter += 1 if c == "(" else (-1 if c == ")" else 0)
    if counter > 0 and operation[-1] not in OPERATORS + ["("]:
        operation += ")"
    return operation, last_operation, answer

def func(operation, last_operation, answer, name):
    if len(operation) == 0 or operation[-1] in OPERATORS + ["("]:
        operation += name + "("
    return operation, last_operation, answer