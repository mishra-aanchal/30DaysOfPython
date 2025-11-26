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
#Split the string 'AI For All' using space as the separator (split()) .
print(company.split(' '))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))
#What is the character at index 0 in the string AI For All.
print(company.index[0]) # this won't work, as here, you are treating company.index (a function) like a list or string. index is a method, and methods cannot be subscripted — that’s why Python gives error
print(company[0])
#What is the last index of the string AI For All.
print(company.rindex('l'))
#What character is at index 5 in "AI For All" string.
print(company[5])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
full_word = 'Python For Everyone'
acronym = full_word.split()
acronym = ''
print(acronym)
#Use index to determine the position of the first occurrence of A in AI For All.
print(company.index('A'))
#Use index to determine the position of the first occurrence of F in AI For All.
print(company.index('F'))
#Use rfind to determine the position of the last occurrence of l in AI For All People.
print(company.rfind('l'))


