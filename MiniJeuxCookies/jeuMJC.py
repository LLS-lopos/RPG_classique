from classes.personnage.villageois.p_mamie import Mamie
from fonction_mod.utile.F_compteur_tour import compteur_tour
from interface.interface.affichage_texte import affichage_texte


def game_cookie():
    affichage_texte("Le Jeu De Fabrication de CooKie", "Cuisine")
    tour = 0
    cookie = 0
    recrue = 3
    mamie = 0
    group_mamie = []
    total_mamie = []
    while True:
        tour = compteur_tour(tour)
        affichage_texte([f"1 - préparer cookie   (cookie: {cookie})", f"2 - acheter une mamie ({recrue}-cookie)"],
                        f"Tour ({tour})", "Objectif 100 cookie")
        entrer = input("Que faire ?\n>>> ")
        if group_mamie:
            for i in group_mamie:
                prod = i.cookie_produit()
                cookie += prod
            for i in group_mamie:
                retrait = i.retraite()
                if retrait:
                    group_mamie.remove(i)
                    total_mamie.append(i)

        if entrer == "1":
            print(f"Vous préparé 1 cookie")
            cookie += 1
        elif entrer == "2":
            if recrue > cookie:
                print(f"vous n'avez pas assez de cookie ({cookie}) pour recruter une mamie ({recrue}-cookie)")
                continue
            else:
                print(f"Vous avez recruter une mamie, il vous reste {cookie} cookie")
                cookie -= recrue
                mamie += 1
                var = Mamie(("Mamie " + str(mamie)))
                group_mamie.append(var)
                affichage_texte(group_mamie, "équipe de mamie")
                recrue += 3
                print(f"Votre groupe mamie est de {mamie} !")
        else:
            pass
        print(f"Vous avez {cookie} cookies")
        if cookie >= 100:
            print("Jeu Fini")
            total_mamie += group_mamie
            affichage_texte(total_mamie, "équipe de mamie")
            break
