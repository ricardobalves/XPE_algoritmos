import numpy as np

#Create an array with 2 rows and 3 columns
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Original Array:")
print(arr)

#Inserting Elements
#Insert 7 at 3rd position
arr = np.insert(arr,2,7)

print("\nArray after inserting 7:")
print(arr)

#Deleting Elements
#Delete 5th position element
arr = np.delete(arr,4)

print("\nArray after deleting 5th position element:")
print(arr)


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr = np.insert(arr, 1, 55, axis=1)
print('axis: \n' ,arr)

#https://numpy.org/doc/stable/reference/generated/numpy.insert.html
#append
#Append elements at the end of an array.

#concatenate
#Join a sequence of arrays along an existing axis.

#delete
#Delete elements from an array.
#%%
