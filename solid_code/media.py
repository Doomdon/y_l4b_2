from abc import abstractmethod, ABC
from places import Place
from heroes import SuperHero


class Media(ABC):
    @abstractmethod
    def create_news(self, place: Place, hero: SuperHero):
        pass


class NewsPaper(Media):
    def create_news(self, place: Place, hero: SuperHero):
        print(f"Print in the newspaper: {hero.name} saved the {place.name()}")


class TV(Media):
    def create_news(self, place: Place, hero: SuperHero):
        print(f"News on the TV: {hero.name} saved the {place.name()}")
