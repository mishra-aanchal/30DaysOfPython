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