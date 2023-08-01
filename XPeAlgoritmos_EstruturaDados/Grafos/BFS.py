def bfs(grafo, inicio):
    visitado = []
    fila = []

    fila.append(inicio)
    visitado.append(inicio)

    while fila:
        atual = fila.pop(0)
        print(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado.append(vizinho)

# Grafo representado como um dicionário
grafo = {
    'A': ['B', 'C', 'E'],
    'B': ['A','D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B','D'],
    'F': ['C'],
    'G': ['C']
}

bfs(grafo, 'A')
#%%
