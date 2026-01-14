from classes.vegetation.agricole.mais import Mais
from classes.vegetation.agricole.truffe import Truffe
from classes.vegetation.nature.pommier import Pommier
from fonction_mod.utile.F_compteur_tour import compteur_tour
from interface.interface.affichage_texte import affichage_texte

Actions = [
    "1 Planter du maïs",
    "2 Planter un pommier",
    "3 Planter une truffe",
    "4 Récolter toutes les plantes mûres",
    "5 Attendre",
    "6 Quitter"]


def farming_ferme():
    culture_plante = []
    jour = 0
    piece = 0
    affichage_texte("Bienvenue dans le jeu", "Ferme Farming")
    a = [Pommier(), Truffe(), Mais()]
    print("\n\n")
    affichage_texte(a, "Ma Belle Végétation")
    while True:
        jour += compteur_tour(jour)
        affichage_texte(Actions, f"Jour {jour} - Objectif 100 Pièce ({piece})")
        print()
        affichage_texte(([f"Pièce: {piece}/100", f"Cuture:"]+culture_plante), "état de la partie")
        choix = input("Quoi faire ?\n>>> ")
        if choix == "1":
            print(Actions[0][2:])
        elif choix == "2":
            print(Actions[1][2:])
        elif choix == "3":
            print(Actions[2][2:])
        elif choix == "4":
            print(Actions[3][2:])
        elif choix == "5":
            print(Actions[4][2:])
            continue
        elif choix == "6":
            print(Actions[5][2:])
            break

