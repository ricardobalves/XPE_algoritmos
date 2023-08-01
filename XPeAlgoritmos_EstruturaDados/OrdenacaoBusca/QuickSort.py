def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        iguais  = [x for x in lista if x == pivo]
        menores = [x for x in lista if x <  pivo]
        maiores = [x for x in lista if x >  pivo]
        return quick_sort(menores) + iguais + quick_sort(maiores)

lista = [5,3,1,7,4,9,2]

print(quick_sort(lista))
#%%
