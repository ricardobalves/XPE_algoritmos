def pos_ordem(arvore):
    if arvore:
        pos_ordem(arvore.esquerda)
        pos_ordem(arvore.direita)
        print(arvore.valor)

# Teste

# Árvore
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Root Node
root = No(1)

# Nós da esquerda
root.esquerda = No(2)
root.esquerda.esquerda = No(4)
root.esquerda.direita = No(5)

# Nós da direita
root.direita = No(3)
root.direita.esquerda = No(6)
root.direita.direita = No(7)

# Percorrer Árvore
pos_ordem(root)

# Saída
# 4
# 5
# 2
# 6
# 7
# 3
# 1
#%%
