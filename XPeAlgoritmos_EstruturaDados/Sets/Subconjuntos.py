def subconjunto(conjunto_a, conjunto_b):
    conjunto_resultante = conjunto_a.intersection(conjunto_b)
    return conjunto_resultante


conjunto_a = set([0, 1, 2, 3, 4, 5])
conjunto_b = set([2, 4, 6, 8])
print(subconjunto(conjunto_a, conjunto_b))

#%%
