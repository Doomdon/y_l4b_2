from abc import ABC, abstractmethod


class Place(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def antagonist(self):
        pass


class Kostroma(Place):
    def name(self):
        return 'Kostroma'

    def antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    def name(self):
        return 'Tokyo'

    def antagonist(self):
        print('Godzilla stands near a skyscraper')
