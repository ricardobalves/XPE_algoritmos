# fatorial com recursao
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print('O fatorial é: ', fatorial(4))


