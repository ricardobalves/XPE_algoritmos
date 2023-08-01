def subconj(conjunto, subconjunto):
    contador = 0
    for elemento in subconjunto:
        if elemento in conjunto:
            contador += 1
    if contador == len(subconjunto):
        return True
    else:
        return False

conjunto = {1, 2, 3, 4, 5, 6}
subconjunto = {2, 4, 6}

if(subconj(conjunto, subconjunto)):
    print("É um Subconjunto")
else:
    print("Não é um subconjunto")

#%%
