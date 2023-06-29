import cProfile

def cProfile_Test():
    # create a list of 1 million random numbers
    my_list = [np.random.rand() for _ in range(1000000)]
    
    # multiply each element of the list by 2
    for i in range(len(my_list)):
        my_list[i] = my_list[i] * 2

cProfile.run('cProfile_Test')