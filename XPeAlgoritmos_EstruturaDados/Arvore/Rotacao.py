# Definir a classe Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Definir a função de rotação
def rotate(root, direction):
    if direction == 'left':
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
    elif direction == 'right':
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
    return newRoot


# Definir a função de percorrer a estrutura
def traverse(root):
    if root is None:
        return
    traverse(root.left)
    print(root.data)
    traverse(root.right)


# Exemplo de árvore de rotação
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Rotação
root = rotate(root, 'left')

# Percorrer a árvore
traverse(root)


#%%
