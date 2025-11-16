#string: Any data type written as text is a string. 
#Any data under single, double or triple quote are strings.
message = 'Hello World'
print(message)
print(len(message))

#Multiline string is created by using triple single (''') or triple double quotes (""")
multiline_message = '''I am an educator and enjoy teaching.
I love building communities, and meeting like minded people.'''
print(multiline_message)
#or
multiline_message = """I am a educator and enjoy teaching.
I love building communities, and meeting like minded people."""
print(multiline_message)

#String Concatenation

first_name = 'Aanchal' 
last_name = 'Mishra'
space = ' '
full_name = first_name + space + last_name
print(first_name)
print(len(first_name))
print(len(last_name))
print(len(full_name))

#escape sequences
print('I am dora the explorer\n: what about you?')
print('Days\tTopics\tExercises')
print('day1\t2\t4')
print('day2\t4\t8')
print('day3\t8\t16')
print('this is a back slash symbol\\:')
print('Every programming language starts with \"Hello, World\"')

#Old Style String Formatting (% Operator)
first_name = 'Aanchal'
last_name = 'Mishra'
formatted_string = 'My name is %s %.s' %(first_name,last_name)
#new style string formatting(str.format) - introduced in Python version 3.
#1st example
first_name = 'Aanchal'
last_name = 'Mishra'
language = 'Python'
formatted_string = 'I am {} {}. I am learning {}'.format(first_name, last_name, language)
print(formatted_string)
#2nd example
a = 5
b = 10
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{}*{} ={}'.format(a,b,a*b))
print('{}/{} ={}'.format(a,b,a/b))
print('{}%{} ={}'.format(a,b,a%b))
print('{}//{} ={}'.format(a,b,a//b))
print('{}**{} ={}'.format(a,b,a**b))

#another new string formatting - String Interpolation (python 3.6+)
a = 2
b = 4
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} // {b} = {a//b}')

