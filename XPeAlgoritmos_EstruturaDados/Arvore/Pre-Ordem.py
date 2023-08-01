def preordem(arvore):
  if arvore:
    print(arvore.valor)
    preordem(arvore.esquerda)
    preordem(arvore.direita)

class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

# criação da árvore
raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

# chamada da função
preordem(raiz)

# saída: 1 2 4 5 3
#%%
