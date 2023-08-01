import numpy as np

array = np.array([1,2,3,4,5])

array_new = np.roll(array, -3)
print(array_new)


#%%
# -----------------------------

# Create an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Shift elements to the right
shift_arr = np.roll(arr, -2)
print("\nArray shifted 2 elementos para a esquerda: ", shift_arr)

# Shift elements to the left
shift_arr = np.roll(arr, 2)
print("\nArray shifted 2 elementos para a direita: ", shift_arr)
#%%
