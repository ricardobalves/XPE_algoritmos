dicionario = {
    'nome': 'Ana',
    'idade': 25,
    'cidade': 'São Paulo'
}

# Usando get - retorna o valor associado a chave
print(dicionario.get('nome'))

# Usando item - retorna uma lista de tuplas, onde cada tupla é composta de uma chave e valor do dicionário
print(dicionario.items())

# Usando keys - retorna uma lista com todas as chaves do dicionário
print(dicionario.keys())

# Usando values - retorna uma lista com todos os valores do dicionário
print(dicionario.values())

# Usando pop - retorna e remove o valor associado a chave
print(dicionario.pop('idade'))

print(dicionario)
#%%
