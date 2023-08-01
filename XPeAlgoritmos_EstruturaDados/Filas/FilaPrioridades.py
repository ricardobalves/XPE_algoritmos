# Inicializando a fila de prioridades
import heapq

fila = []

# Inserindo elementos na fila de prioridades
heapq.heappush(fila, (4, 'A'))
heapq.heappush(fila, (3, 'B'))
heapq.heappush(fila, (2, 'C'))
heapq.heappush(fila, (1, 'D'))
heapq.heappush(fila, (5, 'E'))

# Removendo elementos da fila de prioridades
print(heapq.heappop(fila))   # Saída: (1, 'D')
print(heapq.heappop(fila))   # Saída: (2, 'C')
print(heapq.heappop(fila))   # Saída: (3, 'B')
print(heapq.heappop(fila))   # Saída: (4, 'A')
print(heapq.heappop(fila))   # Saída: (5, 'E')
#%%
