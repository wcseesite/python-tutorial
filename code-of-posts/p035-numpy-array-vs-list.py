import numpy as np
import time

# create a list of 1 million random numbers
my_list = [np.random.rand() for _ in range(1000000)]

# create a numpy array of 1 million random number
my_array = np.random.rand(1000000)

# multiply each element of the list by 2
start = time.time()
for i in range(len(my_list)):
    my_list[i] = my_list[i] * 2
end = time.time()
list_time = end - start

# multiply each element of the numpy array by 2
start = time.time()
my_array = my_array * 2
end = time.time()
array_time = end - start

print('List time:', list_time)
print('Array time:', array_time)