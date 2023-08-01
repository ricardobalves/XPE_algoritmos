#importar bibliotecas
from collections import deque

#definir a classe Grafo
class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacentes = [[] for _ in range(num_vertices)]

    def adiciona_aresta(self, v1, v2):
        self.adjacentes[v1].append(v2)
        self.adjacentes[v2].append(v1)

    def exibe_adjacentes(self, v):
        print(self.adjacentes[v])

    def bfs_recur(self, raiz, alvo):

        # cria uma fila e insere o nó raiz
        fila = deque([raiz])

        # cria um array de visitados
        visitados = [False] * self.num_vertices

        # marca a raiz como visitada
        visitados[raiz] = True

        # loop enquanto a fila não estiver vazia
        while fila:

            # remove o primeiro elemento da fila
            v = fila.popleft()

            # checa se o elemento atual é o alvo
            if v == alvo:
                return True

            # percorre todos os adjacentes de v
            for i in self.adjacentes[v]:
                if visitados[i] == False:
                    # marca o adjacente como visitado
                    visitados[i] = True
                    # adiciona o adjacente à fila
                    fila.append(i)

        return False

#criar um grafo
g = Grafo(4)
g.adiciona_aresta(0, 1)
g.adiciona_aresta(0, 2)
g.adiciona_aresta(1, 2)
g.adiciona_aresta(2, 0)
g.adiciona_aresta(2, 3)
g.adiciona_aresta(3, 3)

#verificar se existe um caminho entre dois vértices
caminho_encontrado = g.bfs_recur(0, 3)

if caminho_encontrado:
    print('Caminho de 0 para 3 encontrado')
else:
    print('Caminho de 0 para 3 não encontrado')
#%%
