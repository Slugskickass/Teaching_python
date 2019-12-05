
count = True                                        # I have defined a variable count and set it to True
                                                    # This allows me to track if a condition has been met later

number = int(input("please give me a number"))      # I ask the user for a number and I store it in a variable
                                                    # Cunningly named number

for I in range(2, number):                          # This for loop runs from 2 to a value 1 before number ( the user
                                                    # Input.  Can you think of a way of making this faster
                                                    # Its maths not programing that will make it faster

    if number % I == 0:                             # The % operator will return the remainder after division
                                                    # So if it is zero we know then number is not a prime number
        count = False                               # If that is the case I set count to be False i.e. not True


if count == True:                                   # Now that my loop has finished I check to see if count is True
    print("prime number")                           # tell the user it is a prime number or ELSE not a prime number
else:
    print("not a prime number")


