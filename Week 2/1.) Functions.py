

def myfunction_one(number_of_iterations):
    for J in range(number_of_iterations):
        for K in range(J):
            print("o", end='')
        print('')

def my_function_two(number_in_one):
    flag = True
    for divisor in range(2,number_in_one):
        if number_in_one % divisor == 0:
            flag = False
    return(flag)

myfunction_one(10)
print('Is the number prime, ', my_function_two(97))
