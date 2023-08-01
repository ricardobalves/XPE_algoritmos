# este programa cria um grafo com lista de adjacência

# classe para representar um vértice
class Vertice:
    def __init__(self, n):
        self.nome = n
        self.vizinhos = list()

    def adicionarVizinho(self, v):
        if v not in self.vizinhos:
            self.vizinhos.append(v)


# classe para representar um grafo
class Grafo:
    vertices = {}

    def adicionarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
            return True
        else:
            return False

    def adicionarAresta(self, u, v):
        if u in self.vertices and v in self.vertices:
            for chave, valor in self.vertices.items():
                if chave == u:
                    valor.adicionarVizinho(v)
                if chave == v:
                    valor.adicionarVizinho(u)
            return True
        else:
            return False

    def imprimirGrafo(self):
        for chave in sorted(list(self.vertices.keys())):
            print(chave + str(self.vertices[chave].vizinhos))


g = Grafo()
a = Vertice('A')
g.adicionarVertice(a)
g.adicionarVertice(Vertice('B'))

for i in range(ord('A'), ord('K')):
    g.adicionarVertice(Vertice(chr(i)))

arestas = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for aresta in arestas:
    g.adicionarAresta(aresta[:1], aresta[1:])

g.imprimirGrafo()
#%%
