import numpy as np

# create a NumPy array
arr = np.array([1,2,3,4,5])

# save the array to a file
np.save('my_array', arr)

# load the array from the file
loaded_arr = np.load('my_array.npy')

# print the loaded array
print(loaded_arr)


# save the array to a text file
np.savetxt('my_array.txt', arr)

# load the array from the text file
loaded_arr = np.loadtxt('my_array.txt')

# print the loaded array
print(loaded_arr)