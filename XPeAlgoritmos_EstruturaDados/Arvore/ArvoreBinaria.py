# definir a classe árvore binária
class ArvoreBinaria:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


# definir a função de pesquisa na árvore binária
def percorrerArvore(raiz):
    # Se a árvore estiver vazia
    if raiz == None:
        return

    # Primeiro imprima o valor da raiz
    print(raiz.valor),

    # Então percorra a subárvore esquerda
    percorrerArvore(raiz.esquerda)

    # Depois percorra a subárvore direita
    percorrerArvore(raiz.direita)


# criar a árvore
raiz = ArvoreBinaria(1)
raiz.esquerda = ArvoreBinaria(2)
raiz.direita = ArvoreBinaria(3)
raiz.esquerda.esquerda = ArvoreBinaria(4)
raiz.esquerda.direita = ArvoreBinaria(5)

# percorrer a árvore
percorrerArvore(raiz)
#%%
