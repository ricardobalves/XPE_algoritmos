nums = set([1, 2, 2, 3, 3, 3])
# apesar do 4 não existir, não retorna erro
nums.discard(4)
nums.discard(2)
print(nums)
#%%
