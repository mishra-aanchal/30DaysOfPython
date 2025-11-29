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
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
veggies = ['capsicum','bitterguard', 'onion', 'potato', 'tomato']
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

#Accessing List Items Using Positive Indexing
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
print(fruits[0])
#this will give correct answer, but this is a better approach :
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)
# Why it's good: Useful when you want to use first_fruit later in the code
second_fruit = fruits[1]
print(second_fruit)
last_index = len(fruits) -1
last_fruit = fruits[last_index]
print(last_fruit)

#Accessing List Items Using Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
veggies = ['capsicum','bitterguard', 'onion', 'potato', 'tomato']
second_lastveg = veggies[-2]
print(second_lastveg)

#Unpacking List Items
Friends = ['Aanchal', 'Hashini', 'Yashi', 'Anwesha', 'Bharvi', 'Ketki']
first_friend, second_friend, third_friend, *rest = Friends
print(first_friend)



