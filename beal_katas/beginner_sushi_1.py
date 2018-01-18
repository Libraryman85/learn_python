import random
name = input('What is your name?')
my_number = input('Hello ' + name + ' What is your number?')
my_number = int(my_number) + random.randint(1,100)
print('Your hashed number is ' + str(my_number))
