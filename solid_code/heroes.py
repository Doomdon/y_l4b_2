from places import Place
from abc import ABC, abstractmethod


def find(place: Place):
    place.antagonist()


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    @staticmethod
    def find(place: Place):
        place.antagonist()

    @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass


# mixins
class Gun:
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class Laser:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class Kick:
    @staticmethod
    def roundhouse_kick():
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
