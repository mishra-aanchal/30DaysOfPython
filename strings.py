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

#Reversing a string

message = "Hello World"
reverse_language = message[::-1]
print(reverse_language)

#logic behind [::-1] - this is in format [ start: stop: step]
#In [::-1] -> start - not given -> start from the end
#stop -> not given -> got to the beginning
#step -> move backwards by 1 charecter.
#hence, the slice means - Start from the last character and move backward one step at a time until the string ends.

#skipping characters while slicing

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

#String methods

#capitalize()
sentence = 'Strings is a vast topic'
print(sentence.capitalise())

#count()
sentence = 'Strings is a vast topic'
print(sentence.count('s'))
print(sentence.count('s',4,15))
#this will give result - 2 reason - Counts 's' only between index 4 (inclusive) and 15 (exclusive), where it appears 2 times.
#format of the string is str.count(substring, start, end)-> in this case ('s',4,15)

#endswith() Checks if a string ends with a specified ending
sentence = 'Strings is a vast topic'
print(sentence.endswith('pic'))

#exapandtabs()
line = 'Strings\tis\ta\tvast\ttopic'
print(line.expandtabs(3))
# expandtabs() replaces each \t with spaces; default tab size = 8, or use expandtabs(n) for custom width

#find() Returns the index of the first occurrence of a substring, if not found returns -1
line = 'Strings is a vast topic'
print(line.find('n'))
print(line.find('funcn'))

#rfind() Returns the index of the last occurrence of a substring, if not found returns -1
line = 'Strings is a vast topic'
print(line.rfind('i'))

#format()
name = 'Aanchal'
role = 'Developer Advocate'
org = 'Postman'
line = 'I am {}. I am a {} at {}.'.format(name,role,org)
print(line)

#index() Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
idea = 'build an AI agent'
sub_string = 'AI'
print(idea.index(sub_string))
print(idea.index(sub_string, 'bu'))
print(idea.index(sub_string, 8))

#rindex() Returns the highest index of a substring. additional arguments indicate starting and ending index (default 0 and string length - 1)
idea = 'build an AI agent'
sub_string = 'AI'
print(idea.index(sub_string))

#isalnum() Checks alphanumeric character
idea = 'buildtwentyAIagents'
print(idea.isalnum())
idea = 'build 20 ai agents' #False, space is not an alphanumeric character
print(idea.isalnum())
idea = 'build20aiagents'
print(idea.isalnum())

#isalpha() Checks if all string elements are alphabet characters (a-z and A-Z)
idea = 'Build APIs' #False, space not alpha
print(idea.isalpha())
idea = 'BuildAPIs'
print(idea.isalpha())
idea = 'Build2APIs'
print(idea.isalpha())

#isdecimal()
phrase = '123'
print(phrase.isdecimal())
phrase = '123go'
print(phrase.isdecimal())
phrase = '1 2 3 G0'
print(phrase.isdecimal()) #False - space not allowed

#isdigit()
digit = '123'
print(digit.isdigit())
digit = 'onetwothree'
print(digit.isdigit())
digit = '123②'
print(digit.isdigit())

#isnumeric() Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '12'
print(num.isnumeric())
num = '\u00BD' #1/2
print(num.isnumeric())
num = '15.5'
print(num.isnumeric())

#isidentifier() it checks if a string is a valid variable name
var = 'LetsDoIt'
print(var.isidentifier())
var = 'LetsDoIt1cemore'
print(var.isidentifier())
var = '1cemore'
print(var.isidentifier()) #False, because it starts with a number



