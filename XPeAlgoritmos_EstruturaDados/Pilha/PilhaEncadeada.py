class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""
    def __init__(self):
        self.topo = None
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    def inserir(self, novo_dado):
        """Insere um elemento no final da pilha."""
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo
        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo
    def remover(self):
        """Remove o elemento que está no topo da pilha."""
        assert self.topo, "Impossível remover valor de pilha vazia."
        self.topo = self.topo.anterior

# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.
for i in range(5):
    pilha.inserir(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

# Remove elementos na pilha.
while pilha.topo != None:
    pilha.remover()
    print("Removendo elemento que está no topo da pilha: ", pilha)

#%%

#%%
