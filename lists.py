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
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(rest)
print(tenth)
Cities = ['Mumbai', 'Noida', 'Bangalore', 'Hyderabad', 'Trivandrum', 'Goa', 'Pondicherry', 'Patna']
MH, DL, KA, HY,KL, *rest, GA, BR = Cities
print(MH)

#Slicing items from list - We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
all_fruits = fruits[0:4] #it returns all the fruits
all_fruits = fruits[0:] #if we don't set where to stop it takes all the rest
leechee_and_mango = fruits[0:2] 

#negative indexing - We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
all_fruits = fruits[-4:]
all_fruits = fruits[0:]
apple_pineapple = fruits[-2:]

#Modifying Lists

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
fruits[0] = 'Avacado'
last_index = len(fruits) -1
fruits[last_index] = 'Guava'

#Checking items in a list - Checking an item if it is a member of a list using in operator. See the example below.
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
does_exist = 'orange' in fruits
print(does_exist)
does_exist = 'Leechee' in fruits
print(does_exist)

#Adding Items to a List - To add item to the end of an existing list we use the method append().
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
fruits.append('Berry')
print(fruits)
fruits.append('Guava')
print(fruits)

#Inserting Items into a List - We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
# syntax
#lst = ['item1', 'item2']
#lst.insert(index, item)

fruits = ['Leechee', 'mango', 'apple', 'pineapple']
fruits.insert(2, 'guava')
print(fruits)

#Removing Items from a List - The remove method removes a specified item from a list
#syntax
#lst = ['item1', 'item2']
#lst.remove(item)

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.remove('guava')

#Removing Items Using Pop
#The pop() method removes the specified index, (or the last item if index is not specified):
# syntax
#lst = ['item1', 'item2']
#lst.pop()       # last item
#lst.pop(index)

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.pop()
fruits.pop(2)

#Removing Items Using Del
#The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
# syntax
# lst = ['item1', 'item2']
# del lst[index] # only a single item
# del lst        # to delete the list completely


# Clearing List Items - The clear() method empties the list:
# syntax
#lst = ['item1', 'item2']
#lst.clear()

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.clear()

#Copying a List
'''It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. 
Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. 
But there are lots of case in which we do not like to modify the original instead we like to have a different copy. 
One of way of avoiding the problem above is using copy().'''

fruits = ['Leechee', 'mango', 'guava', 'apple', 'pineapple']
fruits.copy()
