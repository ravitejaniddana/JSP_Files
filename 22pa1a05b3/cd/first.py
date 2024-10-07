gram = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "i"]
}

def removeDirectLR(gramA, A):
    """gramA is dictionary"""
    temp = gramA[A]
    temper = []
    templnCr = []

    for i in temp:
        if i[0] == A:
            templnCr.append(i[1:] + [A + "'"])
        else:
            temper.append(i + [A + "'"])

    temper.append(["e"])
    gramA[A] = temper
    gramA[A + "'"] = templnCr
    return gramA

def checkForIndirect(gramA, a, ai):
    if ai not in gramA:
        return False
    if a == ai:
        return True
    for i in gramA[ai]:
        if i[0] == ai:
            return False
        if i[0] in gramA:
            return checkForIndirect(gramA, a, i[0])
    return False

def rep(gramA, A):
    temp = gramA[A]
    newTemp = []

    for i in temp:
        if checkForIndirect(gramA, A, i[0]):
            t = []
            for k in gramA[i[0]]:
                t += k
            t += i[1:]
            newTemp.append(t)
        else:
            newTemp.append(i)

    gramA[A] = newTemp
    return gramA

def rem(gram):
    C = 1
    conv = {}
    gramA = {}
    revconv = {}

    for j in gram:
        conv[C] = j 
        gramA[j] = []  
        C += 1

    for i in gram:
        for j in gram[i]:
            temp = []
            for k in j:
                if k in conv:
                    temp.append(k) 
                else:
                    temp.append(k)  
            gramA[i].append(temp)

    for i in range(len(gram)):
        ai = list(gram.keys())[i]
        for j in range(0, i):
            aj = list(gram.keys())[j]
            if ai != aj:
                if aj in gramA and checkForIndirect(gramA, ai, aj):
                    gramA = rep(gramA, ai)

    for i in range(len(gram)):
        ai = list(gram.keys())[i]
        for j in gramA[ai]:
            if ai == j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    return gramA

result = rem(gram)

def first(gram, term):
    a = []
    if term not in gram:
        return [term]
    for i in gram[term]:
        if i[0] not in gram:
            a.append(i[0])
        elif i[0] in gram:
            a += first(gram, i[0])
    return list(set(a))  

firsts = {}
for i in result:
    firsts[i] = first(result, i)
    print(f"First({i}):", firsts[i])

def follow(gram, term, visited=None):
    if visited is None:
        visited = set()
    a = []
    
    for rule in gram:
        for production in gram[rule]:
            if term in production:
                index = production.index(term)
                
                if index + 1 < len(production):
                    next_symbol = production[index + 1]
                    
                    if next_symbol in firsts:
                        next_firsts = firsts[next_symbol]
                        a += [f for f in next_firsts if f != 'e']
                        
                        if 'e' in next_firsts:
                            a += follow(gram, rule)  
                    else:
                        a.append(next_symbol)  

                if index + 1 == len(production) or (index + 1 < len(production) and production[index + 1] == 'e'):
                    if rule not in visited:
                        visited.add(rule)
                        a += follow(gram, rule, visited)  

    return list(set(a)) 

follows = {}
for i in result:
    follows[i] = follow(result, i)
    follows[i] += ["$"]  
    print(f"Follow({i}):", follows[i])