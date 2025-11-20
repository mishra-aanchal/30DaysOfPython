num = '12'
print(num.isnumeric())
num = '\u00BD' 
print(num.isnumeric())
num = '15.5'
print(num.isnumeric())
var = 'LetsDoIt'
print(var.isidentifier())
var = 'LetsDoIt1cemore'
print(var.isidentifier())
var = '1cemore'
print(var.isidentifier())