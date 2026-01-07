import pathlib

from classes.personnage.perso import Personnage

hero = Personnage("XANA", 20, 0, 3, 4)

# dossier
home = pathlib.Path.home()
save_game = home / ".RPG_CLASSIQUE"

# fchier

if not save_game.exists():
    save_game.mkdir()

def sauve_player(personnage):
    personnage.niveau_sup(20)
    personnage.sauvegarde()

def chager_player(personnage):
    personnage.charger()

print(hero)
sauve_player(hero)
chager_player(hero)
print(hero)