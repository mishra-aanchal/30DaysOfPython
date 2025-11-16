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

#Python strings as sequences of charecters
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Accessing charecters in strings by Index 
'''In programming counting starts from zero. 
Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.'''

#['P', 'Y', 'T', 'H', 'O', 'N']
#  0 ,  1 ,  2 ,  3 ,  4 ,  5

language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
third_letter = language[2]
print(third_letter)
fourth_letter = language[3]
print(fourth_letter)
fifth_letter = language[4]
print(fifth_letter)
sixth_letter = language[5]
print(sixth_letter)

#if we want to strt from right hand, we can use negative indexing

language = 'Python'
last_letter = language[5]
print(last_letter)
second_last = language[4]
[print(second_last)]

#slicing python strings

language = 'Python'
last_three_letters = language[-3:]
print(last_three_letters)

language = "python"

first_three = language[0:3]  
last_three = language[3:]     

full_word = first_three + last_three

print(first_three, last_three)  
print(full_word)  
print(f'{first_three} + {last_three} = {full_word}')