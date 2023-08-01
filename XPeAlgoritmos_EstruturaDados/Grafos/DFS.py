
# Programa de busca em profundidade

# Classe de nó para ajudar a construir o grafo
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.adjacentes = []

# Grafo usado para testar o algoritmo
grafo = [Node(1), Node(2), Node(3), Node(4), Node(5)]
grafo[0].adjacentes = [grafo[1], grafo[2]]
grafo[1].adjacentes = [grafo[2], grafo[3]]
grafo[2].adjacentes = [grafo[3], grafo[4]]
grafo[3].adjacentes = [grafo[4]]

# Função de busca em profundidade
def buscaProfundidade(inicio, fim):
    # Pilha de nós a visitar
    stack = [inicio]

    # Lista de nós visitados
    visitados = []

    while len(stack) > 0:
        n = stack.pop()

        if n not in visitados:
            visitados.append(n)

            # Se achamos o nó fim, a busca termina
            if n == fim:
                return True

            # Adicionamos todos os nós adjacentes não visitados à pilha
            for adjacente in n.adjacentes:
                if adjacente not in visitados:
                    stack.append(adjacente)

    # Se a pilha estiver vazia, chegamos ao fim da busca sem sucesso
    return False

# Testando
print(buscaProfundidade(grafo[0], grafo[4])) # True
print(buscaProfundidade(grafo[1], grafo[0])) # False
#%%
