# Criando a classe Árvore Binária Balanceada
class BinaryTree:
    # Inicializando a Árvore
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    # Método para inserir nós na Árvore
    def inserir(self, valor):
        # Se o valor for maior do que o nó raiz, insere a direita
        if valor > self.valor:
            if self.direita is None:
                self.direita = BinaryTree(valor)
            else:
                self.direita.inserir(valor)
        # Se o valor for menor do que o nó raiz, insere a esquerda
        elif valor < self.valor:
            if self.esquerda is None:
                self.esquerda = BinaryTree(valor)
            else:
                self.esquerda.inserir(valor)

    # Método para percorrer a Árvore Binária
    def percorrer(self):
        # Percorrendo a Árvore pela esquerda
        if self.esquerda is not None:
            self.esquerda.percorrer()

        # Printando os valores
        print(self.valor)

        # Percorrendo a Árvore pela direita
        if self.direita is not None:
            self.direita.percorrer()


# Criando a Árvore
arvore = BinaryTree(10)

# Inserindo os nós na Árvore
arvore.inserir(5)
arvore.inserir(20)
arvore.inserir(15)
arvore.inserir(2)
arvore.inserir(7)

# Percorrendo a Árvore
arvore.percorrer()
#%%
