# lista de presidentes americanos
us_presidents_list = ['Joe Biden', 'Donald Trump', 'Barack Obama', 'Barack Obama', 'George W. Bush', 'George W. Bush']

for president in us_presidents_list:
    print(president)
#Acessando um item da lista
print("")
print(us_presidents_list[1],'\n')

#Modificando listas
us_presidents_list.append('Bill Clinton')
print(us_presidents_list, end='\n')

#Alterando
print("")
us_presidents_list[4] = 'George Bush'
print(us_presidents_list, '\n')

#Removendo
us_presidents_list.remove('Bill Clinton')
print('\n',us_presidents_list)


#%%
