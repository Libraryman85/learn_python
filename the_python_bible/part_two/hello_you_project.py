# Ask user their name
# Ask user for age
# Ask user city
# Ask user what they enjoy
# create output text
# print output to screen
name = input('What is your name?: ')

age = input('How old are you?: ')

city = input('What city do you live in?: ')

love = input('What is your favorite hobby?: ')

# str() to turn int into str
# for example turns int 1 into str "1"
# format function
# "{} - {}"
# add .format

string = 'Your name is {} and you are {} years old. You live in {} and you love {}'

output = string.format(name, age, city, love)

print(output)
