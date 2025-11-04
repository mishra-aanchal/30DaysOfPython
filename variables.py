#variables must start with a letter or underscore
#variable can't start with a number
#variables name can't have special characters like !, @, #, $, %, etc.
#variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
#variable names are case-sensitive (firstname, Firstname and FIRSTNAME are three different variables)
#The equal sign (=) is used to assign values to variables.

#Printing variable values stored in the variables
first_name = "Aanchal"
last_name = "Mishra"
Country = "India"
Skills = ["HTML", "CSS", "JavaScript", "Python"]
print('First Name:', first_name)
print('Last Name:', last_name)
print("Country:", Country) 
print("Skills:", Skills)

#Derclaring multiple variables in one line
First_name, last_name, country = 'Aanchal', 'Mishra', 'India'
print(First_name)
print(last_name)
print(country)

#assigning data we get from user into variables using input() function
First_name = input("Enter your first name: ")
country = input("Enter your country: ")
print(First_name)
print(country)