#A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

#In python we can create lists in 2 ways:
#1. using build-in funcn
list = list()
empty_list = list() #this is an empty list, no item in the list
print(len(empty_list)) #0

#2. using []
list = []
empty_list = [] #this is an empty list, no item in the list
print(len(empty_list)) #0

#Lists with initial values. We use len() to find the length of a list.
fruits = ['Leechee', 'mango', 'apple', 'apple', 'pineapple']
veggies = ['capcicum','bitterguard', 'onion', 'potato', 'tomato']
diary_products = ['milk', 'butter', 'meat', 'yogurt']
languages = ['JS', 'Python', 'java', 'ruby']
countries = ['India', 'USA', 'Switzerland', 'Norway']
print("Aanchal's fav fruits:", fruits)
print('Number of fruits:', len(fruits))
print("Aanchal's fav veggies:", veggies)
print('Number of veggies:', len(veggies))
print('Diary Products :', diary_products)
print('Number of diary products:', len(diary_products))
print("Aanchal wishes to visit these Countries:", countries)
print('Number of countries:',len(countries))

#Lists can have items of different data types
list = ['Aanchal', 100, True, {'County':'India', 'city':'Tamil Nadu'}] # list containing different data types
print(list)

