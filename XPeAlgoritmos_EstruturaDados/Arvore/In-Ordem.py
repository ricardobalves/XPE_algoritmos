# Definir a classe Nó
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    # Percorrer a Árvore em Ordem In-Ordem


def inOrder(root):
    if root:
        # Percorrer a Árvore In-Ordem esquerda
        inOrder(root.left)

        # Imprimir o Nó atual
        print(root.val)

        # Percorrer a Árvore In-Ordem direita
        inOrder(root.right)

    # Criar uma Árvore Binária


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
#%%
