from solve import solve

def number(op, op_scorsa, ans, n):
    return op+str(n), op_scorsa, ans

def canc(op, op_scorsa, ans):
    return "", "", ans

def virgola(op, op_scorsa, ans, OPERATORS):
    segno = False
    ultima_virgola = -1
    for i in range(len(op)):
        if op[i] == ".":
            ultima_virgola = i
    if ultima_virgola == -1:
        segno = True
    else:
        for i in range(ultima_virgola, len(op)):
            if op[i] in OPERATORS:
                segno = True
    
    if op != "" and op[-1] in [str(i) for i in range(10)] and segno:
        op += "."
        
    return op, op_scorsa, ans

def delete(op, op_scorsa, ans):
    return op[:-1], op_scorsa, ans

def segno(op, op_scorsa, ans, segno):
    if op != "" and op[-1] in [str(i) for i in range(10)]:
        op += segno
    return op, op_scorsa, ans

def uguale(op, op_scorsa, ans, OPERATORS):
    if op != "" and op[-1] in [str(i) for i in range(10)]:
        op_scorsa = op + "="
        op = solve(op, OPERATORS)
        ans = op
        return op, op_scorsa, ans

def ans(op, op_scorsa, ans, OPERATORS):
    if len(op) == 0 or op[-1] in OPERATORS:
        op += str(ans)
    return op, op_scorsa, ans

def altro(op, op_scorsa, ans):
    return op, op_scorsa, ans

def sinistra(op, op_scorsa, ans):
    return op, op_scorsa, ans

def destra(op, op_scorsa, ans):
    return op, op_scorsa, ans