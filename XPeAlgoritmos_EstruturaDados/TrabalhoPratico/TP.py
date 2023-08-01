# Prática 01 - listas
lista_compras = ["arroz", "feijão", "ovo", "leite"]

# imprimir a lista
print(lista_compras)

# adicionar um item
lista_compras.append("cebola")

# imprimir a lista
print(lista_compras)

# remover um item
lista_compras.remove("ovo")

# imprimir a lista
print(lista_compras)

# alterar um item
lista_compras[1] = "macarrão"

# imprimir a lista
print(lista_compras)

# comandos adicionais
# adicionar um item
lista_compras.append("batata")
# alterar um item
lista_compras[3] = "requeijão"
print(lista_compras)

#%%
#Prática 02 - Arrays

array = [1,2,3,4,5]

#imprimir o conteúdo do array
for i in array:
    print(i)

#acessar o segundo item
print(array[1])

#atualizar o segundo item
array[1] = 6
print(array[1])

#adicionar mais um item ao array
array.append(7)
print(array)

#remover o último item
array.pop()
print(array)

#comando adicional
for j in array:
  print(array)
  array.pop()
print ("Resultado", array)
#%%
# Prática 03 com Pilha
def push():
    pilha.append(item)

def pop():
    if len(pilha) == 0:
        return None
    else:
        return pilha.pop()

pilha = [4,5,6,9,7]

while True:
    item = int(input("Digite o número a ser adicionado à pilha: "))
    push()
    print(pilha)
    escolha = input("Deseja remover o último item? (s/n)")
    if escolha == 's':
        pop()
        print(pilha)
    else:
        break


#%%
# Prática 04 com Fila Circular

# criar a lista vazia
fila = []

# definir o tamanho da fila
MAX_TAM = 5

# criar um cursor para a fila
# começa no primeiro elemento da fila
cursor = 0

# função para adicionar elementos na fila
def adicionar(elemento):
    if len(fila) < MAX_TAM:
        fila.append(elemento)
        print(f'O elemento {elemento} foi adicionado na fila.')
    else:
        print('A fila está cheia!')

# função para remover elementos da fila
def remover():
    global cursor
    if len(fila) > 0:
        elemento = fila.pop(cursor)
        print(f'O elemento {elemento} foi removido da fila.')
        # atualizar o cursor para o próximo elemento
        cursor = (cursor + 1) % MAX_TAM
    else:
        print('A fila está vazia!')

# função para exibir os elementos da fila
def exibir():
    print('Elementos da fila:', fila)

# adicionar elementos na fila
adicionar(10)
adicionar(20)
adicionar(30)
adicionar(40)
adicionar(50)
adicionar(60)

# exibir os elementos da fila
exibir()

# remover elementos da fila
remover()
remover()
remover()

# exibir os elementos da fila
exibir()

#%%
