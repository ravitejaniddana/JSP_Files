gram = {
    "E": ["2E2", "3E3", "4"]
}

starting_terminal = "E"
inp = "2324232$"

stack = "$"
print(f"{'Stack': <15} {'I': <1} {'Input Buffer': <15} {'I': <1} {'Parsing Action'}")
print(f"{'-':-<50}")

while True:
    action = True
    i = 0
    while i < len(gram[starting_terminal]):
        if gram[starting_terminal][i] in stack:
            stack = stack.replace(gram[starting_terminal][i], starting_terminal)
            print(f"{stack: <15} {'1': <1} {inp: <15} {'I': <1} Reduce -> {gram[starting_terminal][i]}")
            i = -1
            action = False
            break  # Break to restart the outer loop

        i += 1

    if len(inp) > 1:
        stack += inp[0]
        inp = inp[1:]
        print(f"{stack: <15} {'1': <1} {inp: <15} {'I': <1} Shift")
        action = False

    if inp == "$" and stack == ("$" + starting_terminal):
        print(f"{stack: <15} {'l': <1} {inp: <15} {'l': <1} Accepted")
        break

    if action:
        print(f"{stack: <15} {'l': <1} {inp: <15} {'l': <1} Rejected")
        break