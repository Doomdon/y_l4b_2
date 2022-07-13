from media import NewsPaper, TV
from heroes import ChackNorris, Superman, SuperHero
from places import Kostroma, Place, Tokyo


def save_the_place(hero: SuperHero, place: Place, papers: NewsPaper, tv: TV):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    papers.create_news(place, hero)
    tv.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPaper(), TV())
    print('-' * 54)
    save_the_place(ChackNorris(), Tokyo(), NewsPaper(), TV())
    print('-' * 54)
