# Example_2
# Define a string
str ='Hello'                                # Define a string

print(str[0])                               # Print the first character
print(str[1])                               # Print the second character
print(str[2])                               # Print the third character
print()
new_str = str[4] + str[3] + str[2] + str[1] + str[0]
print(new_str)
print()
#Notice that python starts counting at 0

fox = 'fox'
#Define a list
my_list =['The', 'silly', fox]            # This is a list, simply the things you want between square backets
print(my_list[1])                           # Each item in the list can be addressed
print()
print(my_list[2][0])                        # Each SUB item in the list can be addressed
print(my_list[2][1])
print(my_list[2][2])
print()


my_complex = complex(1,1)
my_name = 'Ashley'
my_int = 1
my_float = 1.0
my_list = [my_complex, my_name, my_int, my_float]       # We can define a list as a variety of things
print(my_list)                                          # Print the things
my_list[3] = 'Testing'                                  # We can change one of the values.
print(my_list)
my_list.append("last one")                              # This is how we add a term to the end
print(my_list)


# Define a tuple
my_tuple = (my_complex, my_name, my_int, my_float)
print(my_tuple)
print()
print()

# Define a dictionary
my_dictionary = { 'Name': 'Ashley', 'Position': 'Researcher', 'Employee Number': 101}
# To build a dictionary we

print(my_dictionary)
X = my_dictionary['Name']
print(X)
print(my_dictionary.keys())
print(my_dictionary.values())
