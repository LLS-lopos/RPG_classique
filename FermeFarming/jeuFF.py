from classes.vegetation.agricole.mais import Mais
from classes.vegetation.agricole.pomme import Pomme
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
    vendu = []
    culture_arbre = []
    culture_plante = []
    element = 0
    jour = 0
    piece = 0
    affichage_texte("Bienvenue dans le jeu", "Ferme Farming")
    while True:
        jour = compteur_tour(jour)
        etat = [f"Pièce: {piece}/100"]

        if culture_plante != []:
            etat += ["Culture:"]
            for i in culture_plante:
                i.check_mure()
            etat += culture_plante
        if culture_arbre != []:
            etat.append("Arbre:")
            for i in culture_arbre:
                i.check_mure()
                if i._mure:
                    fruit = i.apparition_pomme()
                    for pomme in range(fruit):
                        element += 1
                        pomme = Pomme(("Pomme " + str(element)))
                        culture_plante.append(pomme)
                    etat += culture_plante
            etat += culture_arbre

        affichage_texte(Actions, f"Jour ({jour})", f"Objectif 100 Pièce ({piece})")
        affichage_texte(etat, "Mini Farming Simulator", "état de la partie")

        choix = input("Quoi faire ?\n>>> ")
        if choix == "1":
            print(Actions[0][2:])
            element += 1
            var = Mais()
            culture_plante.append(var)
        elif choix == "2":
            print(Actions[1][2:])
            element += 1
            var = Pommier()
            culture_arbre.append(var)
        elif choix == "3":
            print(Actions[2][2:])
            element += 1
            var = Truffe()
            culture_plante.append(var)
        elif choix == "4":
            print(Actions[3][2:])
            for i in culture_plante[:]:
                if i._mure == True:
                    piece += i.vendre()
                    culture_plante.remove(i)
                    vendu.append(i)
        elif choix == "5":
            print(Actions[4][2:])
            continue
        elif choix == "6":
            print(Actions[5][2:])
            break

        if piece >= 250:
            log_ven = len(vendu)
            log_autre = len(culture_plante)
            vendu += culture_plante
            vendu += culture_arbre
            affichage_texte(vendu, "Fin De La Partie", f"Stats: pièce->{piece}, non vendu->{log_autre}, plantes vendu->{log_ven}, nombre de jour->{jour}")
            break

