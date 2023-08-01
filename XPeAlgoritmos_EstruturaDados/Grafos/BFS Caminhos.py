# Algoritmo de busca em largura

# Esta função retorna um array de caminhos mais curtos a partir de um nó inicial
def busca_em_largura(grafo, inicio):

    # Mantemos uma fila para armazenar os nós que precisam ser verificados
    fila = [inicio]

    # Criamos um array para armazenar os caminhos mais curtos
    caminhos_mais_curto = []

    # Mantemos um dicionario para armazenar os nós que já foram verificados
    visitados = {inicio: None}

    # Enquanto a fila não estiver vazia
    while fila:

        # Retiramos o primeiro nó da fila
        vertice = fila.pop(0)

        # Adicionamos o nó a lista de caminhos mais curtos
        caminhos_mais_curto.append(vertice)

        # Para cada vizinho deste nó
        for vizinho in grafo[vertice]:

            # Se o nó não foi visitado
            if vizinho not in visitados:

                # Marque-o como visitado e adicione-o à fila
                visitados[vizinho] = vertice
                fila.append(vizinho)

    # Retorne a lista de caminhos mais curtos
    return caminhos_mais_curto
#%%
