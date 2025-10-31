from random import randint

from fonction_mod.interface.affichage_texte import affichage_texte
from fonction_mod.interface.list_menu import menu_combat


def combat_simple(hero, ennemi):
    while True:
        for i in [hero, ennemi]:
            if i.ko is True:
                return
        print(f"{ennemi.nom} - PV: {"💚" * ennemi.pv}, ⚔️: {ennemi.att}")
        affichage_texte(menu_combat, " Action ")
        choix = input("->")
        if choix == "1":
            hero.attaque(ennemi)
        elif choix == "2":
            print(f"{hero.nom} ne fait rien")
        elif choix == "3":
            try: hero.utiliser_objet(herbe1, hero)
            except: print("aucun objet")
        elif choix == "4":
            i = randint(1, 5)
            if i == 1:
                break
            else:
                print("L'ennemie vous bloque le passage")
        else:
            print("1 ou 2 comme choix possible")
            continue

        if not ennemi.ko:
            choix_ennemi = randint(0, 5)
            if choix_ennemi < 4:
                ennemi.attaque(hero)
            if choix_ennemi >= 4:
                print(f"{ennemi.nom} ne fait rien")
