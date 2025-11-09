''' Operators in Python are special symbols that carry out arithmetic or logical computation. 
The value that the operator operates on is called an operand. 
For example, in the expression 3 + 2, + is the operator that performs addition on the operands 3 and 2 and other example can be of assignment operator where we use = to assign a value to a variable.'''

# Arithmetic Operators
print(10 + 5)   # Addition
print(10-5)     # Subtraction
print(10 * 5)   # Multiplication
print(10 / 5)   # Division
print(10//3)    #remainder without giving float value
print(10 % 3)   # Modulus, gives the remainder

a = 3
b = 2
total = a+b     #not using sum here as sum is a built-in function in python
diff = a-b 
product = a*b
division = a/b
floor_division = a//b
exponential = a**b

print('a+b =', total)
print('a-b =',diff)
print('a*b =', product)
print('a/b =', division)
print('a//b =', floor_division)
print('a**b =', exponential)
