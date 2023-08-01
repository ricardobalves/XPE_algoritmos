#Inserindo
lista2=['L', 'U', 'Z', 'E', 'S']
lista = ['S', 'C', 'E', 'N', 'D', 'E']
print("Lista original: ", lista)

lista.insert(0, "A")
lista.append("R")
lista.extend(lista2)
print("Inserindo elementos: ", lista)

#Removendo
lista = ['A', 'S', 'C', 'E', 'N', 'D', 'E', 'R']
print("Lista original: ", lista)

lista.remove("S")
print("Removendo um elemento: ", lista)

lista.pop(1)
print("Removendo  elemento: ", lista)


lista.clear()
print("Clear: ", lista)



#%%
