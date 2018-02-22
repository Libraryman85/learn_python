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