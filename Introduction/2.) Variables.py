number_1 = 10
number_2 = 5

temp = number_1 + number_2      # Add the two variables together
print("Addition")               # Print statement
print(temp)                     # Print to result of the addition.
print(type(temp))
print(number_1 + number_2)      # Print the addition directly to the console
print(" ")                      # Print a blank line

temp = number_1 - number_2
print("Subtraction")
print(temp)
print(type(temp))
print(number_1 - number_2)
print(" ")

temp = number_1 * number_2
print("Multiplication")
print(temp)
print(type(temp))
print(number_1 * number_2)
print(" ")

temp = number_1 / number_2
print("Division")
print(temp)
print(type(temp))
print(number_1 / number_2)
print(" ")

print("As a character")
print(chr(number_1 * number_2))             # What is going on here chr is a function that returns the character with ascii value given
print(chr(64))
print(" ")

print("As a complex number")
my_complex = complex(number_1, number_2)    # Form a complex number
print(my_complex)
print(" ")



str = '100'                                         # Define a string

print("int('100') with base 2 = ", int(str, 2))     # Print the string as an integer in base 2
print("int('100') with base 4 = ", int(str, 4))     # Print the string as an integer in base 4
print("int('100') with base 8 = ", int(str, 8))     # Print the string as an integer in base 8
print("int('100') with base 10 = ", int(str, 10))     # Print the string as an integer in base 10
print("int('100') with no base defined = ", int(str))     # Print the string as an integer in base 10
print("int('100') with base 16 = ", int(str, 16))   # Print the string as an integer in Hes


print(float(str))                                   # Print the string as a string
print(bool(str))                                    # Print the string as a boolean
print(complex(str))                                 # Print the string as a complex

