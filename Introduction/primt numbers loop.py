range_of_numbers = int(input('How far do you want me to go ? '))
list_of_primes = []
for test_number in range(range_of_numbers):
    flag = True
    for divisor in range(2, int(test_number**.5)+1):
        if test_number % divisor == 0:
            flag = False
            break
    if flag:
        list_of_primes.append(test_number)
print(list_of_primes)
