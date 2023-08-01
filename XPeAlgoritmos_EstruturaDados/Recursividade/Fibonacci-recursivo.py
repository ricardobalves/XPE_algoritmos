def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def menu():
    n = int(input('Exibir ate o termo (maior que 2): '))
    for val in range(1,n+1):
        print(fibo(val))
while True:
    menu()

#%%
