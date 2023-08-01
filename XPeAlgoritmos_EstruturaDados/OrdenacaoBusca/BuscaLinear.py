def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

lista = [1,3,5,7,9]
valor = 3

posicao = busca_linear(lista, valor)

if posicao == -1:
    print('Valor não encontrado')
else:
    print('Valor encontrado na posição', posicao)