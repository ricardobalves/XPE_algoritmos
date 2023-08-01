fruits = ["Apple", "Mango", "Banana", "Peach"]
for fruit in fruits:
    print(fruit)

#%%
fruits = ["Apple", "Mango", "Banana", "Peach"]
[print(fruit + ' juice') for fruit in fruits]

#%%
fruits = ["Apple", "Mango", "Banana", "Peach"]

# Constructs range object containing elements from 0 to 3
for i in range(len(fruits)):
    print("The list at index", i, "contains a", fruits[i])

#%%
fruits = ["Apple", "Mango", "Banana", "Peach"]

# Constructs range object containing only 1 and 2
for i in range(1, 3):
    print(fruits[i])

#%%
fruits = ["Apple", "Mango", "Banana", "Peach"]

for index, element in enumerate(fruits):
    print(index, ":", element)

#%%
lst1 = [1, 2, 3, 4, 5]
lst2 = []

# Lambda function to square number
temp = lambda i:i**2

for i in lst1:

    # Add to lst2
    lst2.append(temp(i))

print(lst2)

#%%
fruits = ["Apple", "Mango",  "Banana", "Peach"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1
    #i = i + 1

#%%
