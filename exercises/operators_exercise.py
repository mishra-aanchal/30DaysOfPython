#area of circle = pi*r**2
radius = 10
area_of_circle = 3.14*10**2
print('area of this circle =', area_of_circle)

#area of rectangle = l*b
length = 5
width = 10
area_of_rect = length*width
print('area of this rectangle =', area_of_rect)

#weight of an object = mass*gravity
mass = 75
gravity = 9.81
weight = mass*gravity
print('weight of this object is =', weight)

#Exercise
#Declare your age as integer variable
age = 25
print('age:', age)
#Declare your height as a float variable
height = 5.51
print('height:', height)
#Declare a variable that store a complex number
complex_num = 1+2j
print('complex_num:', complex_num)

'''Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle 
(area = 0.5 x b x h).'''

b = float(input('base of triangle:'))
h = float(input('height of triangle:'))
area_of_triangle = 0.5*b*h
print('area of triangle is :', area_of_triangle)

'''Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
Calculate the perimeter of the triangle (perimeter = a + b + c).'''

a =float(input('side a of triangle :'))
b = float(input('side b of triangle :'))
c = float(input('side c of triangle :'))

perim_of_triangle = a + b + c

print('perim of this triangle is:', perim_of_triangle)

'''Get length and width of a rectangle using prompt. 
Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))'''

l = float(input('length of rect is :'))
b = float(input('width of rect is :'))

area_of_rect = l*b
perim_of_rect = 2*(l+b)
print('area of rectangle is :', area_of_rect)
print('perimeter of rectangle is :', perim_of_rect)

'''Get radius of a circle using prompt. 
Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.'''

radius = float(input('radius of the circle is :'))
pi = 3.14
area_of_circle = pi*radius*radius
circum_of_circle = 2*pi*radius
radius = float(input('radius of the circle is :'))
pi = 3.14
area_of_circle = pi*radius*radius
circum_of_circle = 2*pi*radius
print('area of circle is : ', area_of_circle)
print('circumfrence of circle is :', circum_of_circle)




