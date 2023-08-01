def fibonacci(n):
  if n<=1:
    return n
  else:
    return(fibonacci(n-1)+fibonacci(n-2))

n=int(input("Digite um número: "))

if n<=0:
  print("Digite um número positivo")
else:
  for i in range(n):
    print(fibonacci(i))