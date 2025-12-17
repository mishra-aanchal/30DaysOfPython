pos_nums = [1,2,3,4,5]
zero = [0]
neg_nums = [-1, -2, -3, -4, -5]
integers = pos_nums + zero+ neg_nums
print(integers)

list = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
list.extend(vegetables)
print(list)

list = ['banana', 'orange', 'mango', 'lemon']
print(list.count('mango'))

ages = [15, 20, 25, 30, 25]
print(ages.count(25))