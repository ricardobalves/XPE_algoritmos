""" cria array vazio """
temperaturaMedia = []

"""insere elementos """
temperaturaMedia.append(31.9)
temperaturaMedia.append(35.4)
temperaturaMedia.append(26.4)
temperaturaMedia.append(24.3)
temperaturaMedia.append(22.9)

""" imprime array """
print(temperaturaMedia, '\n')

x = 1
soma = 0
for i in temperaturaMedia:
    soma = soma + i
    print(i)
    x+=1
print('A média é: ', soma/x)
#%%

#%%
