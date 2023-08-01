# Função recursivo para encontrar fatorial de um número
def factorial(n):
    fact = 1
    i = 1
    while i < n+1:
        fact = fact * i
        i += 1
    return fact


if __name__ == '__main__':
    n = 5
    print(f'O fatorial de {n} é {factorial(n)}')
#%%
