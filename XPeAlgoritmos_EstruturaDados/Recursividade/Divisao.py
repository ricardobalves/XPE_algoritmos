def Div_ab(a,b):
    if a < b:
        return 0
    else:
        return 1+ Div_ab(a-b, b)

print('Divisao: ', Div_ab(24, 2))
#%%
