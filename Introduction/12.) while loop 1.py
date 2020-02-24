X = 10
while X > 0.001:
    print(X)
    X = X/2

X = 10
test = 0
while X > -0.001:
    print(X)
    X = X/2
    test = test + 1
    if test > 1000:
        break
print('Finished at ', test)


X = 10
test = 0
while X > -0.001 and test < 1000:
    print(X)
    X = X/2
    test = test + 1
print('Finished at ', test)