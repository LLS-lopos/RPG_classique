from random import randint

from classes.personnage.monstre.p_splip import Splip
from classes.personnage.perso import Personnage

def groups_ennemi(max: int):
    n = randint(1, max)
    #print(n)
    groupe = []
    for i in range(n):
        #i = Personnage(nom=f"hero_{i+1}", pv=randint(2, 10), pm=randint(0, 4), att=randint(1, 4), vit=randint(1, 8))
        i = Splip(nom=f"splip {i + 1}", pv=randint(5, 16), pm=3, att=randint(1, 3), vit=randint(2, 10), val_exp=randint(50, 100))
        groupe.append(i)
    return groupe

def groups_hero(max: int):
    n = randint(1, max)
    # print(n)
    groupe = []
    for i in range(n):
        i = Personnage(nom=f"hero_{i+1}", pv=randint(2, 10), pm=randint(0, 4), att=randint(1, 4), vit=randint(1, 8))
        #i = Splip(nom=f"splip {i + 1}", pv=randint(5, 16), pm=3, att=randint(1, 3), vit=randint(2, 10), val_exp=randint(5, 20))
        groupe.append(i)
    return groupe


if __name__ == "__main__":
    ennemy = groups_ennemi(12)
    hero = groups_hero(6)
    for i in hero:
        print(i)
    for i in ennemy:
        print(i)