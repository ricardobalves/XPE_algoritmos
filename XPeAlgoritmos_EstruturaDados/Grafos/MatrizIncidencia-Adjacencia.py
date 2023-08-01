#criando a matriz de adjacencia
matriz_adj = [[0,1,1,0],
              [1,0,1,1],
              [1,1,0,1],
              [0,1,1,0]]

#criando a matriz de incidencia
matriz_inc = [[1,1,0,0],
              [1,0,1,0],
              [0,1,1,1],
              [0,0,1,1]]

#imprimindo as matrizes
print("Matriz de Adjacência")
for linha in matriz_adj:
    print(linha)

print("Matriz de Incidência")
for linha in matriz_inc:
    print(linha)
#%%
