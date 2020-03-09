fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
nuts = ['Pine', 'Cashew', 'Almond', 'Wall']

print('Playing with lists')
print(fruits)
print('Add a pineapple to the list')
fruits.append('Pineapple')
print(fruits)
print('Extend a list to the list')
fruits.extend(nuts)
print(fruits)
print('Inset an obect in to a position')
fruits.insert(4, 'Passion')
print(fruits)
print('Remove an item')
fruits.remove('Pine')
print(fruits)
print('There are ', fruits.count('apple'),'apples')
# - list.append(x)
# - list.extend(iterable)
# - list.insert(i, x)
# - list.remove(x)
# - list.count(x)

