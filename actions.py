from solve import solve

def number(operation, last_operation, ans, n):
    return operation+str(n), last_operation, ans

def canc(operation, last_operation, ans):
    return "", "", ans

def decimal_point(operation, last_operation, ans, OPERATORS):
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
    
    if operation != "" and operation[-1] in [str(i) for i in range(10)] and sign:
        operation += "."
        
    return operation, last_operation, ans

def delete(operation, last_operation, ans):
    return operation[:-1], last_operation, ans

def sign(operation, last_operation, ans, segno):
    if operation != "" and operation[-1] in [str(i) for i in range(10)] + [")"]:
        operation += segno
    return operation, last_operation, ans

def equals(operation, last_operation, ans, OPERATORS):
    try:
        ans = solve(operation, OPERATORS)
        last_operation = operation + "=" + ans
        operation = ""
    finally:
        return operation, last_operation, ans

def ans(operation, last_operation, ans, OPERATORS):
    if len(operation) == 0 or operation[-1] in OPERATORS:
        operation += str(ans)
    return operation, last_operation, ans

def other(operation, last_operation, ans):
    return operation, last_operation, ans

def left(operation, last_operation, ans):
    return operation + "(", last_operation, ans

def right(operation, last_operation, ans):
    return operation + ")", last_operation, ans