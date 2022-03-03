import json


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each dog
        self.foods = []
        return print(self.name)

    def add_trick(self, trick):
        self.tricks.append(trick)
        return print(self.tricks)

    def add_food(self, food):
        self.foods.append(food)
        return print(self.foods)


d = Dog('Simon')
d.add_trick('Sleeping')
d.add_food('chub')

print(json.dumps(d.__dict__, indent=2))

d.add_trick('drinking tea')
d.add_food('MY SNACKS')
print(json.dumps(d.__dict__, indent=2))
