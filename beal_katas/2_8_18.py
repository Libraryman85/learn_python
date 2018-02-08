# casting changes data types
# print each letter in a given string
print('\n'.join('toast'))
# .join sticks values together
# createa a function that takes an nput, tehn prints each character of the input

def print_characters(input_string):
    for character in input_string:
        print(character)

# create a function tha ttakes 2 inputs, then prints true/false whether or ont the first
# is contained within a second input

text_value = 'some input'
def search_string(search, text_input):
    result = False
    for character in text_input:
        if character == search:
            result = True
    print(result)

search_string('a', text_value)
search_string('s', text_value)
search_string('S', text_value)

