
def myfunction_one(number_of_iterations):               # Here we define the function using the def command and give it
    for J in range(number_of_iterations):               # The ability to accept data in this case a number
        for K in range(J):
            print("o", end='')
        print('')

def my_function_two(number_in_one = 100):               # Again defined by the def command, here we define the default value
    flag = True                                         # Set the prime flag to true
    for divisor in range(2, int(number_in_one**0.5)):   # Move though all the numbers up to the sqrt of the number in question
        if number_in_one % divisor == 0:                # If at any point you get no remainder after division
            flag = False                                # Set the prime flag to false
            break                                       # break the cycle (if its not a prime its not a prime)
    return(number_in_one, flag)                         # We also return a value back to the original program.


# The lines above here do nothing unless the functions are called
# The line below calls myfunction_one and passes it the number 10
#myfunction_one(14)

# The next two lines call my_function_two.
# The first call the function passing the number 97tens
kittens, prime =my_function_two(100000050569)
print(kittens)
print(prime)
print('Is the number prime, ', my_function_two(97))
# If we dont pass a number then normally the function would fail, it would not know what to do.
# However, because we defined the function as def my_function_two(number_in_one = 100): if
# we dont pass a number then it defaults to 100
#print('Is the number prime, ', my_function_two())


# This code allows you to time the amount of time taken for the function to run
# import time
# start = time.time()
# print('Is the number prime, ', my_function_two(100000050569))
# end = time.time()
# print(end-start)

import numpy as np
my_array = np.asarray([1,2,3,4,5,6])