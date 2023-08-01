def somatorio(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + somatorio(n-1)

# Exemplo de uso
print (somatorio(5))

# Saída: 15 (5 + 4 + 3 + 2 + 1)
#%%
