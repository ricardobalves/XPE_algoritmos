# Exemplo de programa em Python para ler e imprimir uma lista de números sem usar dicionários:

# Cria uma lista vazia
lista_numeros = []

# Solicita ao usuário quantos números ele deseja incluir na lista
num_numeros = int(input("Quantos números deseja incluir na lista? "))

# Solicita ao usuário que insira os números na lista
for i in range(num_numeros):
    num = int(input("Insira o número: "))
    lista_numeros.append(num)

# Imprime a lista de números
print("A lista de números incluída é:", lista_numeros)
#%%
