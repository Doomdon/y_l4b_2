from places import Place
from abc import ABC, abstractmethod


def find(place: Place):
    place.antagonist()


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place: Place):
        place.antagonist()

    @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass


# mixins
class Gun:
    def fire_a_gun(self):
        print('PIU PIU')


class Laser:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class Kick:
    def roundhouse_kick(self):
        print('Bump')


class Superman(SuperHero, Laser):

    def __init__(self):
        super().__init__('Clark Kent', True)

    def attack(self):
        print('**Kick**')

    def ultimate(self):
        self.incinerate_with_lasers()


class ChackNorris(SuperHero, Gun):

    def __init__(self):
        super().__init__('Chack Norris', False)

    def attack(self):
        self.fire_a_gun()
