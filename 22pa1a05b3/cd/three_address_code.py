OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2}

def infix_to_postfix(formula):

    stack = []
    output = ""

    for char in formula:
        if char not in OPERATORS:
            output += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() 
        else:
            while stack and stack[-1] != '(' and PRECEDENCE[char] <= PRECEDENCE[stack[-1]]:
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    print(f"POSTFIX: {output}")
    return output

def infix_to_prefix(formula):

    op_stack = []
    exp_stack = []

    for char in formula:
        if char not in OPERATORS:
            exp_stack.append(char)
        elif char == '(':
            op_stack.append(char)
        elif char == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.pop()  
        else:
            while op_stack and op_stack[-1] != '(' and PRECEDENCE[char] <= PRECEDENCE[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.append(char)

    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op + b + a)

    print(f"PREFIX: {exp_stack[-1]}")
    return exp_stack[-1]



def generate_three_address_code(postfix):
    print("### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    temp_var = 1

    for char in postfix:
        if char not in OPERATORS:
            exp_stack.append(char)
        else:
            print(f"t{temp_var} := {exp_stack[-2]} {char} {exp_stack[-1]}")
            exp_stack = exp_stack[:-2]
            exp_stack.append(f"t{temp_var}")
            temp_var += 1


expression = input("INPUT THE EXPRESSION: ")
prefix = infix_to_prefix(expression)
postfix = infix_to_postfix(expression)
generate_three_address_code(postfix)