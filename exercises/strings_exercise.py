#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
space = ' '
concat_string = word1 + space+ word2 + space + word3+ space + word4
print(concat_string)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'AI For All'.
word1 = 'AI'
word2 = 'For'
word3 = 'All'
space = ' '
sentence = word1 + space + word2 + space + word3
print(sentence)

#Declare a variable named company and assign it to an initial value "AI For All".
company = 'AI for All'
#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string AI For All.
print(company.capitalize())
print(company.title())
print(company.swapcase)
#Cut(slice) out the first word of AI For All string.
first_word = company[:2]
print(first_word)
#Check if AI For All string contains a word AI using the method index, find or other methods.
print(company.index('AI'))
# Note: If the word was not in the string it would raise err - ValueError: substring not found, .index() to check presence works only if you expect the substring to exist.
#If you want a safer method, use .find()
print(company.find('AI'))
#Replace the word AI in the string 'AI For All' to Code.
print(company.replace('AI','Code'))
#Change AI for All to Python for everyone using the replace method or other methods.
print(company.replace('AI for All', 'Python for everyone'))