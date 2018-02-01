# strings can be in single or double quotes
# str = 'test'
# str2 = "test"

# string interpolation {}

# bool
# boolean  is true/false
# bool = True
# bool_false = False

# int
# int = 1
# int = -1

# floats are decimals
# float = 1.0
# float_negative = -1.0


# casting
# output = '1' + 1
# to convert string to int
# int('1')
# turn int to str
# (1)

print(bool(0))
print(bool(1))
print(bool(.1))
print(bool('fale'))
print(bool(None))
print(bool([]))

# list data type
_list = ['Alex', 'Grande', 'Sara', 'Danie', 'Laura', 'Jen']

for name in _list:
    print(name)

# for {variable_name} in <collection>:
# <action>

name = 'name'
for character in name:
    print(character)

# Practice: create a function that creates in input, then prints each character of the input

person_name = input('What is your name?: ')

for character in person_name:
    print(character)


def print_character(input):
    for character in input:
        print(character)


print_character('supercalifragilisticexpialidocious')

# == compares
# practice 2: create a function that takes 2 inputs then prints True/False whether or not the first input is contained
# within the second input

def search_character(search,find):
    for character in find:
        if character == search:
            print(True):
      

search_character('a', 'purple')