import numpy as np

# create a 1-dimensional array
a = np.array([1, 2, 3])
print(f'1d:\n {a}\n')

# create a 2-dimensional array
b = np.array([[1,2,3], [4,5,6]])
print(f'2d:\n {b} \n')

# create a 3-dimensional array
c = np.array([[[1,2],[3,4]], [[5,6], [7,8]]])
print(f'3D:\n {c} \n')

# create a 2x3 array of zeros
d = np.zeros((2, 3))
print(f'2x3 arrary of zeros:\n {d} \n')

# create a 2x3 array of ones
e = np.ones((2,3))
print(f'2x3 array of ones:\n {e} \n')

# create a 2x3 array of randon numbers between 0 and 1
f = np.random.rand(2,3)
print(f'2x3 array of ranond number between 0 and 1:\n {f} \n')


# index and slice

# access the first element of a
print(f'first element of a: {a[0]}\n')

# first element of b
print(f'first elemement of b: {b[0][0]}')

# slice b to get the first row
print(f'first row of b: {b[0, :]}\n')

# create a bool array based on a condition
bool_arr = a > 1
print(f'a array is:{a}, bool_arr: {bool_arr} \n')

# use the bool array to select elements from a
print(f'use the bool array to select elements from a: {a[bool_arr]} \n')


# Reshaping ndarrays
# create a 1-dimensional array
g = np.array([1,2,3,4,5,6])
print(f'create 1-d array g: {g} \n')

# reshape g to a 2x3 array
h = g.reshape((2,3))
print(f'reshape g to a 2x3 array h:\n {h} \n')

# reshape h to a 3x2 array
i = h.reshape((3,2))
print(f'reshape h to a 3x2 array i:\n {i} \n')

# flatten i into a 1-d array
j = i.flatten()
print(f'flatten i into 1-d array j:\n {j} \n')

# broadcasting ndarrays
# create a 2x3 array of ones
k = np.ones((2,3))
print(f'create a 2x3 array k:\n {k} \n')

# add 1 to every element in k
l = k + 1
print(f'add 1 to every element in k, the result is l:\n {l} \n')

# add a 1-d array to a 2-d array
m = np.array([1,2,3])
print(f'm:\n{m}\n')

n = k + m

print(f'k + m:\n {n}\n')


# narray attributes
print(f'array n shape is: \n {n.shape} \n')
print(f'array n dtype is: \n {n.dtype}\n')
print(f'array n ndim is:\n {n.ndim}\n')

# narray slicing
arr = np.arange(10)
print(f'arr: \n {arr} \n')

arr_slice = arr[5:8]
print(f'arr_slice: \n {arr_slice} \n')

arr_slice[1] = 66
print(f'arr_slice:\n {arr_slice} \n')
print(f'arr: \n {arr} \n')