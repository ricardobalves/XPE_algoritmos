
# Classe que representa um nó da árvore
class No:
    # Construtor
    def __init__(self, valor):
        self.valor = valor # Valor do nó
        self.esquerda = None # Nó da esquerda (filho)
        self.direita = None # Nó da direita (filho)

# Classe que representa a árvore
class ArvoreBuscaBinaria:
    # Construtor
    def __init__(self):
        self.raiz = None # Nó raiz

    # Método para inserir um nó na árvore
    def inserir(self, valor):
        novoNo = No(valor) # Criando um novo nó

        # Verificando se a raiz é None
        if self.raiz == None:
            self.raiz = novoNo # Inserindo o nó na raiz
            return

        # Variável auxiliar para percorrer a árvore
        atual = self.raiz

        while True:
            # Verificando se o valor é menor que o nó atual
            if valor < atual.valor:
                # Verificando se o nó da esquerda é None
                if atual.esquerda == None:
                    atual.esquerda = novoNo # Inserindo o nó
                    return
                else:
                    atual = atual.esquerda # Atualizando o nó atual
            else:
                # Verificando se o nó da direita é None
                if atual.direita == None:
                    atual.direita = novoNo # Inserindo o nó
                    return
                else:
                    atual = atual.direita # Atualizando o nó atual

# Função para imprimir a árvore em pré-ordem
def imprimirPreOrdem(no):
    # Verificando se o nó é None
    if no != None:
        print(no.valor) # Imprimindo o valor do nó
        imprimirPreOrdem(no.esquerda) # Imprimindo o nó da esquerda
        imprimirPreOrdem(no.direita) # Imprimindo o nó da direita

# Criando a árvore
arvore = ArvoreBuscaBinaria()

# Inserindo os nós na árvore
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(17)

# Imprimindo a árvore em pré-ordem
imprimirPreOrdem(arvore.raiz)
#%%
