# Inserção em listas

#Criando uma lista
lista = [0,1,2,3,4,5,6,7,8,9,101]
#imprimindo a lista
print('\n',lista)

#Usando o comando del
#para remover o elemento na posição 2
del lista[2]
#Imprimindo a lista atualizada
print('\n',lista)

#Usando o comando remove
lista.remove(101)
#Imprimindo a lista atualizada
print('\n',lista)

#Usando o comando pop para
# remover o ultimo elemento da lista
ultimo = lista.pop()
#Imprimindo a lista atualizada
print('\n',lista)
print( ultimo)


#%%
