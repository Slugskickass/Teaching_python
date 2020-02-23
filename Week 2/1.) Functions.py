
def myfunction_one(number_of_iterations):       # Here we define the function using the def command and give it
    for J in range(number_of_iterations):       # The ability to accept data in this case a number
        for K in range(J):
            print("o", end='')
        print('')

def my_function_two(number_in_one = 100):       # Again defined by the def command, here we define the default value
    flag = True
    for divisor in range(2,number_in_one):
        if number_in_one % divisor == 0:
            flag = False
    return(number_in_one, flag)                 # We also return a value back to the original program.

#myfunction_one(10)
#print('Is the number prime, ', my_function_two(97))
print('Is the number prime, ', my_function_two())
