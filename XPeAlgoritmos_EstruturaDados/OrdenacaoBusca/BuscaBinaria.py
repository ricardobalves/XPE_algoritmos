# Implementação de um algoritmo de busca binária em Python

def busca_binaria(lista, item):
    # A lista precisa estar ordenada
    lista_ordenada = sorted(lista)

    baixo = 0
    alto = len(lista_ordenada) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista_ordenada[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


# Testando a busca binária
minha_lista = [1, 3, 5, 7, 9]

print(busca_binaria(minha_lista, 3))  # Retorna 1
print(busca_binaria(minha_lista, -1))  # Retorna None
#%%
