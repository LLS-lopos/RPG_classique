from random import randint

from RPG_Assembly.classe.personnages.ennemie.e_class.Slime import Slime


def generation_ennemie(nombre: int = 1) -> list:
    # ajouter un ou plusieurs types d’ennemis
    if nombre != 1:
        nombre = randint(1, nombre)
    groupe = []
    for i in range(nombre):
        i = Slime()
        groupe.append(i)
    # augmenter leur difficulté
    # tirer un ennemi au hasard
    return groupe
