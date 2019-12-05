from random import randint
value = randint(1, 10)
guess = 0
while guess != value:
    guess = int(input("what is your guess \n"))
    if guess != value:
        print("sorry try again \n")
print('well done')
print(value)

