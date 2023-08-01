cliente = ('Daniella', '123.456.789-11')
#clientes = []
clientes.append(cliente)
#print(clientes)
print(type(clientes))

cliente = ('Jose', '123.456.789-11')
clientes.append(cliente)
print(clientes)
#print(type(clientes))

#clientes = tuple(clientes)

# acessando a tupla
print(clientes[1])
# alterando a tupla
clientes[1] = ('Jose', '222.222.222-22')
print ('tupla alterada ', clientes)
#print(type(clientes))

# transforma a tupla em lista
lista = list(clientes)

#alterando o item na posição 1 da lista
lista[1]= ('Jose', '222.222.222-22')

#transformando a lista em tupla novamente
clientes = tuple(lista)

print(clientes)
#%%
lista = [1,2,3,4,5,1]
tupla = (1,2,3,4,5,1)

print(type(lista))

print(type(tupla))

print(tupla)
print (tupla.index(4))

print (tupla.count(1))

#%%
# Tuplas como Chaves de Dicionários

capitais = {
    ('Brasil', 'Rio de Janeiro'):'Rio de Janeiro',
    ('Brasil', 'Minas Gerais'):'Belo Horizonte',
    ('Brasil', 'São Paulo'):'São Paulo'
}

print(capitais.keys())
print(capitais.values())

#%%
