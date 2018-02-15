import random

class Adventurer:
    def __init__(self, map, name, strength):
        self.map = map
        self.name = name
        self.strength = strength

    def receive_map(self, other_adventurer):
        other_map = other_adventurer.map
        self.map = other_map


def generate_character(map, name):
    strength = random.randint(1, 18)
    adventurer = Adventurer(map, name, strength)
    return adventurer


good_map = 'good map'
bad_map = 'bad map'

alex = generate_character(good_map, 'alex')
sara = generate_character(bad_map, 'sara')
grande = generate_character(good_map, 'grande')
justin = generate_character(bad_map, 'justin')
party = [alex, sara, grande, justin]

for adventurer in party:
    print(adventurer.map + str(adventurer.strength))

sara.receive_map(grande)

print(alex.map)
print(sara.map)
print(grande.map)
print(justin.map)
