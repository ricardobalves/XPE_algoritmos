# isso cria um conjunto vazio
conjunto_A = set()

# isso cria um conjunto com valores
conjunto_B = {1, 2, 3, 4, 5}

# isso adiciona um elemento ao conjunto
conjunto_A.add(10)

# isso cria um conjunto com valores
conjunto_C = {3, 4, 5, 6, 7}

# isso cria um conjunto com a união dos conjuntos
conjunto_uniao = conjunto_B | conjunto_C

# isso cria um conjunto com a diferença entre os conjuntos
conjunto_diferenca = conjunto_B - conjunto_C

# isso cria um conjunto com a intersecção dos conjuntos
conjunto_interseccao = conjunto_B & conjunto_C

# isso cria um conjunto com os elementos que estão em B mas não em C
conjunto_diferenca_simetrica = conjunto_B ^ conjunto_C

# imprime o conjunto de união
print(conjunto_uniao)

# imprime o conjunto de diferenca
print(conjunto_diferenca)

# imprime o conjunto de intersecção
print(conjunto_interseccao)

# imprime o conjunto de diferença simétrica
print(conjunto_diferenca_simetrica)
#%%
