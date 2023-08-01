#incluindo a biblioteca
import queue

#criando a fila
fila = queue.Queue()

#adicionando elementos
fila.put('Elemento 1')
fila.put('Elemento 2')
fila.put('Elemento 3')

#obtendo o tamanho da fila
tamanho = fila.qsize()
print("Tamanho da Fila:", tamanho)

#removendo elementos
print("Removendo elementos da fila:")
while not fila.empty():
    print(fila.get())

#verificando se a fila esta vazia
esta_vazia = fila.empty()
print("A fila esta vazia?", esta_vazia)
#%%
