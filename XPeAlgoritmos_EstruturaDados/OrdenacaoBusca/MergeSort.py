def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Copia os dados para as listas auxiliares
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # Verifica se há algum elemento na lista esquerda
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Verifica se há algum elemento na lista direita
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1


# teste do programa
lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(lista)
print(lista)
#%%
