set_countries = {'col','mex','bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,3,4,4,5,5,6,7,7,7,7,8,9}
print(set_numbers)
print(type(set_numbers))

set_types = {1, 'hola', False, 12.12}
print(set_types)
print(type(set_types))

set_from_string = set('hooola')
print(set_from_string)
print(type(set_from_string))

set_from_tuples = set(('abc', 'dfdf', 'abc', 'grd'))
print(set_from_tuples)
print(type(set_from_tuples))

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)