#importing numpy library
import numpy as np

#creating a numpy array
arr = np.array([1, 2, 3, 4, 5])

#iterating over array
#using nditer()
for x in np.nditer(arr):
    print(x)
#%%
