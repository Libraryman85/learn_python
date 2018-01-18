count = 1
is_continue = True
# if count == 100:
#     print(count)
# elif count == 99:
#     print('pie')
# else:
#     print('nope')
while count<=33:

    if count % 3 == 0:
        print('fizz')
    elif count == 5:
        print('buzz')
    else:
        print(count)
    count = count + 1
