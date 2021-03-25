primes = []
for i in range(2, 1000):
    flag = True
    for J in range(2, i):
        if i % J == 0:
            flag = False
            break
    if flag:
        primes.append(i)
    if len(primes) == 100:
        break
print(len(primes))
