# data type dict {}
# key = value
attendees = ['sara', 'alex', 'justin', 'ryan']

for attendee in attendees:
    # print(attendee)

    employees = {
    'sara': 'csa',
    'alex': 'it support tech',
    'justin': 'software ninja',
    'ryan': 'numbers nerd'
}

print(employees['alex'])
print(employees.get('ilya','russian apy'))

for key in employees:
    print(key + ' - ' + employees[key])

for key, value in employees.items():
    print(key + ' - ' + value)



# def my_method():
#   temp = 1
#
#print(temp)