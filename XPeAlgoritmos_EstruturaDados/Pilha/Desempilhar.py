#Empilha
# Inicia uma pilha – vazia
def init(P):
    P = []

# Empilha novo elemento
def push(P, x):
    P.append(x)

# Retorna o elemento do topo da pilha mas não desempilha
def top(P):
    if is_empty(P):
        return None
    return P[-1]

# Empilha e imprime o estado atual da pilha
def Empilha(p, z):
    push(p, z)
    print(p)

# inicia a pilha
mp = []
init(mp)


#Desempilha
# Remove elemento do topo da pilha
def pop(P):
    if is_empty(P):
        return None
    return P.pop()

# retorna True se a pilha está vazia
def is_empty(P):
    return len(P) == 0

# Desempilha e imprime o estado atual da pilha
def Desempilha(p):
    x = pop(p)
    if x is None:
        print("Vazia")
    else:
        print(p)

# inicia a pilha
mp = []
init(mp)

# operações empilhar

Empilha(mp, 1)
Empilha(mp, "tipo de elemento")
Empilha(mp, (5, 4, 3))
Empilha(mp, True)
print(top(mp))

# operações desempilhar
Desempilha(mp)
Desempilha(mp)
Desempilha(mp)
Desempilha(mp)
Desempilha(mp)
print(top(mp))


#%%
