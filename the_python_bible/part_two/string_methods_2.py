x = 'happy birthday'
x.index('birthday')
# .index counts place where thing begins, beginning with 0

x.find('birthday')
# .find is used to stop program from erroring out, .index is used for hard stop if things go wrong

y = '0000000happybirthday0000000'

y.strip('0')
y.lstrip('0')
y.rstrip('0')
print(y.strip('0'))

name = input('What is your name?: ')
name = (name.strip())
