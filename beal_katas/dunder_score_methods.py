# dunder score methods

# __add__ workds on the + operator
# __eq__ works the = operator
# __str__ works the stro operation
# __init__ the method that is run when a new instance is created


class Adventurer:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name + ' is an awesome person'

sara1 = Adventurer('sara')
sara2 = Adventurer('sara')

print(sara1 == sara2)
print(sara1)
print(sara2)
