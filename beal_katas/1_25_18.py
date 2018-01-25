import sys

message = sys.argv[0]

# str = 'this is a str'
# bool = True # False
# int = 1
# float = 1.0
# if is a control structure
message = 'hello world'
print(message)
# else, not if then. it is if else

# print each letter in a given string
#

#p
#r
#o
#g

message = 'programming 101'

# for <variable_name> in <colletion>
#   <action>
for letter in message:
    print(letter)

# print true or false if a letter exists in a given string

search_value = 'a'

if search_value in message:
    print(True)
else:
    print(False)
message = 'Hello World'
