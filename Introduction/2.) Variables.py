number_1 = 10
number_2 = 5

temp = number_1 + number_2
print("Addition")
print(temp)
print(number_1 + number_2)
print(" ")

temp = number_1 - number_2
print("Subtraction")
print(temp)
print(number_1 - number_2)
print(" ")

temp = number_1 * number_2
print("Multiplication")
print(temp)
print(number_1 * number_2)
print(" ")

temp = number_1 / number_2
print("Division")
print(temp)
print(number_1 / number_2)
print(" ")

print("As a character")
print(chr(number_1 * number_2))             # What is going on here chr is a function that returns the character with ascii value given
print(" ")

print("As a complex number")
my_complex = complex(number_2, number_1)    # Form a complex number
print(my_complex)
print(" ")



str = '100'

print("int('100') with base 2 = ", int(str, 2))
print("int('100') with base 4 = ", int(str, 4))
print("int('100') with base 8 = ", int(str, 8))
print("int('100') with base 16 = ", int(str, 16))


print(float(str))
print(bool(str))
print(complex(str))

