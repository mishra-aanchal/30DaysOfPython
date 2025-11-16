language = 'Python'
last_three_letters = language[-3:]
print(last_three_letters)
first_three = language[0:3]   # stores 'pyt'
last_three = language[3:]     # stores 'hon'

full_word = first_three + last_three

print(first_three, last_three)  
print(full_word)  
print(f'{first_three} + {last_three} = {full_word}')