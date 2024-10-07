gram = {}

# Function to add production to the grammar
def add(s):
    s = s.replace(" ", "").replace("\n", "")
    x = s.split("->")
    gram[x[0]] = x[1].split("|")

# Function to remove direct left recursion
def removeDirectLR(gramA, A):
    alpha, beta = [], []
    for prod in gramA[A]:
        if prod[0] == A:
            alpha.append(prod[1:] + A + "'")
        else:
            beta.append(prod + A + "'")
    gramA[A] = beta
    gramA[A + "'"] = [a for a in alpha] + ["e"]  # "e" represents epsilon (empty string)
    return gramA

# Function to handle indirect left recursion
def replaceIndirect(gramA, A, B):
    new_productions = []
    for prod in gramA[A]:
        if prod[0] == B:
            for prodB in gramA[B]:
                new_productions.append(prodB + prod[1:])
        else:
            new_productions.append(prod)
    gramA[A] = new_productions
    return gramA

# Function to remove both direct and indirect left recursion
def removeLeftRecursion(gram):
    non_terminals = list(gram.keys())

    # Remove indirect left recursion
    for i in range(len(non_terminals)):
        A = non_terminals[i]
        for j in range(i):
            B = non_terminals[j]
            gram = replaceIndirect(gram, A, B)
        
        # Remove direct left recursion
        gram = removeDirectLR(gram, A)
    
    return gram

# Input grammar
n = int(input("Enter No of Productions: "))
for _ in range(n):
    add(input())

# Remove left recursion
result = removeLeftRecursion(gram)

# Print the result
for x, y in result.items():
    print(f"{x} -> {' | '.join(y)}")
