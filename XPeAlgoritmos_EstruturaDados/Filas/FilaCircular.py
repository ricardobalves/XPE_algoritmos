# Declaração de variáveis
fila = []
inicio = 0
fim = 0
tamanho = 5

# Função para adicionar elementos na fila
def inserir(valor):
    global inicio
    global fim
    global fila
    if (fim + 1) % tamanho == inicio:
        print ("A fila está cheia")
    else:
        fila[fim] = valor
        fim = (fim + 1) % tamanho
        print ("Valor inserido com sucesso")

# Função para remover elementos da fila
def remover():
    global inicio
    global fim
    global fila
    if inicio == fim:
        print ("A fila está vazia")
    else:
        valor = fila[inicio]
        inicio = (inicio + 1) % tamanho
        print ("Valor removido: " + str(valor))

# Função para imprimir a fila
def imprimir():
    global inicio
    global fim
    global fila
    if inicio == fim:
        print ("A fila está vazia")
    else:
        indice = inicio
        while indice != fim:
            print (fila[indice])
            indice = (indice + 1) % tamanho

# Função principal
def main():
    global inicio
    global fim
    global fila
    fila = [None] * tamanho
    while True:
        print ("1 - Inserir elemento")
        print ("2 - Remover elemento")
        print ("3 - Imprimir fila")
        print ("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            valor = int(input("Digite o valor a ser inserido: "))
            inserir(valor)
        elif opcao == 2:
            remover()
        elif opcao == 3:
            imprimir()
        else:
            break

# Chamada da Função principal
main()
