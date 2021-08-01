def solve(operazione, OPERATORS):
    operatori = []
    pos_operatori = []
    to_pop = []
    for i in range(len(operazione)):
        if operazione[i] in OPERATORS:
            operatori.append(operazione[i])
            pos_operatori.append(i)
    list1 = list(operazione)
    for i in pos_operatori:
        list1[i] = " "
    if list1[0] == " ":
        list1.insert(0, "0")
    operazione = "".join(list1)
    operazione = operazione.split()
    for i in range(len(operazione)):
        operazione[i] = float(operazione[i])

    for i in range(len(operatori)):
        if operatori[i] == "^":
            operazione[i - len(to_pop)] **= float(operazione[i + 1 - len(to_pop)])
            operazione.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    i = len(to_pop) - 1
    while i >= 0:
        operatori.pop(to_pop[i])
        i -= 1

    to_pop = []

    for i in range(len(operatori)):
        if operatori[i] == "x":
            operazione[i - len(to_pop)] *= float(operazione[i + 1 - len(to_pop)])
            operazione.pop(i + 1 - len(to_pop))
            to_pop.append(i)
        elif operatori[i] == "/":
            operazione[i - len(to_pop)] /= float(operazione[i + 1 - len(to_pop)])
            operazione.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    i = len(to_pop) - 1
    while i >= 0:
        operatori.pop(to_pop[i])
        i -= 1

    to_pop = []

    for i in range(len(operatori)):
        if operatori[i] == "+":
            operazione[i - len(to_pop)] += float(operazione[i + 1 - len(to_pop)])
            operazione.pop(i + 1 - len(to_pop))
            to_pop.append(i)
        elif operatori[i] == "-":
            operazione[i - len(to_pop)] -= float(operazione[i + 1 - len(to_pop)])
            operazione.pop(i + 1 - len(to_pop))
            to_pop.append(i)

    operazione = str(operazione[0])
    if operazione[-2:] == ".0":
        operazione = operazione[0:-2]
    split = operazione.split("e")
    if len(split) == 1:
        operazione = split[0]
    else:
        operazione = split[0] + "x10^" + split[1][1:]
    return operazione