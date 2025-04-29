from random import randint

from classes.monstre.p_splip import Splip
from classes.perso import personnage


def groups_ennemi(max: int):
    n = randint(1, max)
    #print(n)
    groupe = []
    for i in range(n):
        #i = personnage(nom=f"ennemi_{i+1}", pv=random.randint(2, 10), att=random.randint(1, 4))
        i = Splip(nom=f"splip {i + 1}", pv=randint(5, 16), att=randint(1, 3), val_exp=randint(5, 20))
        groupe.append(i)
    return groupe

if __name__ == "__main__":
    groups_ennemi(12)