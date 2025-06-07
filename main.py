from math import atan
from classes.monstre.p_splip import Splip
from classes.objet.classique.herbe import HerbeMedicinal1
from classes.perso import Personnage
from fonction_mod.FM_groupe_ennemi import groups_ennemi
from fonction_mod.M_combat_equipe import combat
from fonction_mod.M_combat_simple import combat_simple
from fonction_mod.M_combat_un_contre_group import combat_un_contre_group
from fonction_mod.affichage_texte import affichage_texte
from fonction_mod.list_menu import accueil, mode

herbe1 = HerbeMedicinal1()

group1 = groups_ennemi(10)


def boucle_de_jeu():
    print(" RPG ADVENTURE CLASSIQUE CLI")
    while True:
        affichage_texte(accueil)
        choix = input("-> ")
        if choix == "1":
            mode_jeu()
        elif choix == "2":
            print("Style donjon crawler et hack and slash")
        elif choix == "3": test()
        elif choix == "4": break
        else: continue


def mode_jeu():
    while True:
        HERO = Personnage("XANA", 60, 3, 4)
        ins_splip = Splip(att=6)
        affichage_texte(mode)
        mode_de_jeu = input("-> ")
        if mode_de_jeu == "1":
            combat_simple(HERO, ins_splip)
        elif mode_de_jeu == "2":
            combat_un_contre_group(HERO, group1)
        elif mode_de_jeu == "3":
            combat([HERO], group1)
        elif mode_de_jeu == "4": break
        else: continue

def test():
    print(f"Instance {herbe1}")
    HERO = Personnage("XANA", 60, 3, 4)
    ins_splip = Splip(att=6)
    HERO.__repr__()
    HERO.remplir_sac(herbe1)
    HERO.remplir_sac(herbe1)
    HERO.remplir_sac(herbe1)
    ins_splip.attaque(HERO)
    ins_splip.attaque(HERO)
    ins_splip.attaque(HERO)
    HERO.voir_contenue_sac()
    HERO.utiliser_objet(herbe1, HERO)

    HERO.voir_contenue_sac()
    HERO.__repr__()

if __name__ == '__main__':
    boucle_de_jeu()
