for I in range(10):
    print(I)
print()


for snuggle in range(20, 30, 2):
    print(snuggle)
print()

X = [1, 2, 3, 4, 5, 'Hello', 6, 7, 8, 'World']
for I in X:
    print(I)

for X in range(10):
    for Y in range(10):
        print(Y, end='')
    print(' ', end = '')

for X in range(10):
    for Y in range(X):
        print(Y, ' ', end = '')
    print()
