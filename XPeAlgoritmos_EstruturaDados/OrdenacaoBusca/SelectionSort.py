def selection_sort(lista):
    for i in range(len(lista)):
        # Acha o menor elemento na lista desordenada
        menor_elemento = i
        for j in range(i + 1, len(lista)):
            if lista[menor_elemento] > lista[j]:
                menor_elemento = j

        # Troca o elemento menor achado com o primeiro elemento
        lista[i], lista[menor_elemento] = lista[menor_elemento], lista[i]


lista = [3, 7, 2, 9, 1, 4]
selection_sort(lista)

print(lista)
#%%
