class Heroes:
    def __init__(self, name, move):
        self.name = name
        self.health = 0
        self.move = move

    def health_add(self, add_health):
        self.health += add_health

    def health_minus(self, minus_health):
        self.health -= minus_health

    def say_name(self):
        print(self.name)

    def get_health(self):
        return self.health

    def get_move(self):
        return self.move


class Bowman(Heroes):
    def shot_distance(self):
        print("I can hit targets at a distance")


class Doctor(Heroes):
    def healing(self):
        print("I can heal myself and other heroes")


class Grunt(Heroes):
    def fight(self):
        print("I can fight in close combat")


hero_1 = Bowman('Arthur', 'I can move to right and left')
hero_2 = Doctor('Blackman', 'I can move to straight, right, left')
hero_3 = Grunt('Bin', 'I can move to right, straight and back')


hero_1.health_add(4)
hero_1.health_minus(0.8)
hero_1.health_minus(0.02)
hero_1.health_add(7)
print(hero_1.say_name(), hero_1.get_health(), hero_1.move, hero_1.shot_distance())

hero_2.health_add(10)
hero_2.health_minus(0.9)
print(hero_2.say_name(), hero_2.move, hero_2.get_health(), hero_2.healing())


hero_3.health_add(1)
hero_3.health_minus(0.03)
print(hero_3.say_name(), hero_3.move, hero_3.get_health(), hero_3.fight())


