# class encapsulates behavior and staet

import random


class Adventurer:
    def __init__(self, map, name, equipment: dict):
        self.map = map
        self.name = name
        self.hat = equipment['hat']
        self.shoes = equipment['shoes']

    def __str__(self):
        return 'I am {self.name}. I wear {self.hat} hat and {self.shoes} shoes'


class Hat:
    def __init__(self, style: str):
        self.style = style

    def a_method(self):
        pass

    def __str__(self):
        return self.style


hat1 = Hat('beanie')
hat2 = Hat('sports cap')
hat3 = Hat('fedora')


default_equipment = {
    'hat' : Hat('peasant'),
    'shoes' : None
}


    # def receive_map(self, other_adventurer):
    #     other_map = other_adventurer.map
    #     assert isinstance(other_map)
    #     self.map = other_map
    #




hats = [hat1, hat2, hat3]

for hat in hats:
    print(hat)


# def generate_character(map, name):
#     strength = random.randint(1, 18)
#     adventurer = Adventurer(map, name, strength)
#     return adventurer
#
#
# good_map = 'good map'
# bad_map = 'bad map'
#
# alex = generate_character(good_map, 'alex')
# sara = generate_character(bad_map, 'sara')
# grande = generate_character(good_map, 'grande')
# justin = generate_character(bad_map, 'justin')
# party = [alex, sara, grande, justin]
#
# for adventurer in party:
#     print(adventurer.map + str(adventurer.strength))
#
# sara.receive_map(grande)
#
# print(alex.map)
# print(sara.map)
# print(grande.map)
# print(justin.map)
