fruits = ['Leechee', 'mango', 'apple', 'pineapple']
all_fruits = fruits[-4:]
all_fruits = fruits[0:]
apple_pineapple = fruits[-2:]
print(all_fruits)
print(apple_pineapple)

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
fruits[0] = 'Avacado'
last_index = len(fruits) -1
fruits[last_index] = 'Guava'
print(fruits)
fruits[3] = 'berry'
print(fruits)

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
does_exist = 'orange' in fruits
print(does_exist)
does_exist = 'Leechee' in fruits
print(does_exist)

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
fruits.append('Berry')
print(fruits)
fruits.append('Guava')
print(fruits)

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
fruits.insert(2, 'guava')
print(fruits)

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.remove('guava')
print(fruits)

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.pop()
fruits.pop(2)

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.clear()
print(fruits)

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits_copy = fruits.copy()
print(fruits_copy)