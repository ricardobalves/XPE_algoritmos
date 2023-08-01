def soma(pilha):

    # Se a pilha estiver vazia, retorne 0
    if len(pilha) == 0:
        return 0
    # Remova o último elemento da pilha
    last = pilha.pop()
    # Chame recursivamente a função soma
    result = last + soma(pilha)
    # Insira o elemento removido de volta na pilha
    pilha.append(last)

    return result

# Driver Code
pilha = [1, 2, 3, 4]
print(soma(pilha))
#%%
