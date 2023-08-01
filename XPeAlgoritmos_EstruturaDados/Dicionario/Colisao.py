hash_table = [None] * 10
print (hash_table)

# função calcula a chave pela key passada % (modulo) tamanho do hash table
def hashing_func(key):
    return key % len(hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value


print (hashing_func(10)) # Output: 0
print (hashing_func(20)) # Output: 0
print (hashing_func(25)) # Output: 5


insert(hash_table, 10, 'Nepal')
print (hash_table)
# Output:
# ['Nepal', None, None, None, None, None, None, None, None, None]

insert(hash_table, 25, 'USA')
print (hash_table)
# Output:
# ['Nepal', None, None, None, None, 'USA', None, None, None, None]

insert(hash_table, 20, 'India')
print (hash_table)
# Output:
# ['India', None, None, None, None, 'USA', None, None, None, None]
