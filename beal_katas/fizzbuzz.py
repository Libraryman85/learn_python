count = 1
is_continue = True
while count<=33:

    if count % 3 == 0:
        print('fizz')
    elif count == 5:
        print('buzz')
    else:
        print(count)
    count = count + 1
