sentence = 'Strings is a vast topic'
print(sentence.endswith('pic'))
line = 'Strings\tis\ta\tvast\ttopic'
print(line.expandtabs(3))
line = 'Strings is a vast topic'
print(line.find('n'))
print(line.find('th')) 
line = 'Strings is a vast topic'
print(line.rfind('i'))
name = 'Aanchal'
role = 'Developer Advocate'
org = 'Postman'
line = 'I am {}. I am a {} at {}.'.format(name,role,org)
print(line)
idea = 'build an AI agent'
sub_string = 'AI'
print(idea.index(sub_string))
print(idea.index(sub_string, 8))