# função recursiva para calcular o fatorial de um número
def fatorial(num):
    if num <= 1:
        return 1
    else:
        return num * fatorial(num - 1)

# função principal do programa
def main():
    for i in range(5+1):
        print("%2d! = %d" % (i, fatorial(i)))

if __name__== "__main__":
    main()


#%%
