idea = 'build an AI agent'
sub_string = 'AI'
print(idea.index(sub_string))
print(idea.index(sub_string, 8))
idea = 'build an AI agent'
sub_string = 'nt'
print(idea.index(sub_string))
idea = 'buildtwentyAIagents'
print(idea.isalnum())
idea = 'build20aiagents'
print(idea.isalnum())
idea = 'Build APIs'
print(idea.isalpha())
idea = 'BuildAPIs'
print(idea.isalpha())
idea = 'Build2APIs'
print(idea.isalpha())
phrase = '123'
print(phrase.isdecimal())
phrase = '123go'
print(phrase.isdecimal())
phrase = '1 2 3 G0'
print(phrase.isdecimal())
digit = '123'
print(digit.isdigit())
digit = 'onetwothree'
print(digit.isdigit())
digit = '123②'
print(digit.isdigit())
