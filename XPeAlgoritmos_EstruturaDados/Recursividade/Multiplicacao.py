def Mult_ab(a,b):
    if b == 0:
        return b
    elif b == 1:
        return a
    else:
        return a + Mult_ab(a, b - 1)

print('Multiplicacao: ', Mult_ab(3, 2))
#%%
