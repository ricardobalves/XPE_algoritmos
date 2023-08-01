# Função recursiva para encontrar fatorial de um número
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


if __name__ == '__main__':
    n = 5
    print(f'O fatorial de {n} é {factorial(n)}')

#%%

#%%
