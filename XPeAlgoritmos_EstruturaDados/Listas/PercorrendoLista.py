inicio = 0
fim = 100
passo = 10


lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

#Acessando o elemento na posição 2
print('posicao2 :', lista[2])

# Convertendo um intervalo em uma lista.
print(list(range(inicio, fim, passo)))



#%%
# Ordenando listas.
lista = [7, 25, 2, 3, 30, 7, 80, 100, -1, 15]
print("Lista não ordenada: ", lista)

lista.sort()
print("Lista ordenada: ", lista)

lista.sort(reverse=True)
print("Lista ordenada em ordem decrescente: ", lista)
