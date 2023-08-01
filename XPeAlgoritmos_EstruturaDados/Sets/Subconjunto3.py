def subconjunto(lista):
    resultado = []
    for i in range(0, len(lista)+1):
        for j in range(i + 1, len(lista)+1):
            subconj = lista[i:j]
            resultado.append(subconj)
    return resultado

lista = [2, 3, 4, 5]
print(subconjunto(lista))
#%%
