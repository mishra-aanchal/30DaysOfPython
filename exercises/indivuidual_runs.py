veggies = ['capsicum','bitterguard', 'onion', 'potato', 'tomato']
second_lastveg = veggies[-2]
print(second_lastveg)
first_veg = veggies[-5]
print(first_veg)

Friends = ['Aanchal', 'Hashini', 'Yashi', 'Anwesha', 'Bharvi', 'Ketki']
first_friend, second_friend, third_friend, *rest = Friends
print(first_friend)
print(second_friend)
print(third_friend)
print(rest)
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
Cities = ['Mumbai', 'Noida', 'Bangalore', 'Hyderabad', 'Trivandrum', 'Goa', 'Pondicherry', 'Patna']
MH, DL, KA, HY, *rest, GA, PY, BR = Cities
print(MH)
print(DL)
print(KA)
print(HY)
print(rest)
fruits = ['Leechee', 'mango', 'apple', 'pineapple']
all_fruits = fruits[0:4]
leechee_and_mango = fruits[0:2]
print(leechee_and_mango)
print(all_fruits)


