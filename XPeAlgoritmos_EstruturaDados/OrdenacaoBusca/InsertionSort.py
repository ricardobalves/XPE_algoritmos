def insertionSort(lista):
    for indice in range(1, len(lista)):
        chave_atual = lista[indice]
        posicao = indice

        while posicao > 0 and lista[posicao - 1] > chave_atual:
            lista[posicao] = lista[posicao - 1]
            posicao = posicao - 1
        lista[posicao] = chave_atual

lista = [54,26,93,17,77,31,44,55,20]
insertionSort(lista)
print(lista)
#%%
