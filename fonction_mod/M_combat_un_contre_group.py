from random import randint

from fonction_mod.affichage_texte import affichage_texte
from fonction_mod.list_menu import menu_combat


def combat_un_contre_group(hero, ennemy: list):
    adver_list = ennemy[:]
    perso_ko = []
    while True:
        # Afficher l'état des ennemis
        for ennemi in adver_list: print(f"{ennemi.nom} - PV: {"💚"*ennemi.pv}, ⚔️: {ennemi.att}")

        # Vérifier si tous les ennemis sont KO
        if len(adver_list) <= 0: return print("Tous les ennemis sont KO !")
        affichage_texte(menu_combat, " Action ")
        choix = input("-> ")
        if choix == "1":
            # Afficher les ennemis disponibles pour l'attaque avec leur index
            for index, ennemi in enumerate(adver_list):
                print(f"{index} - {ennemi.nom} PV={ennemi.pv} ATT={ennemi.att}")
            try:
                adversaire_index = int(input("Choisissez un adversaire: "))
                if 0 <= adversaire_index < len(adver_list):
                    ennemi_cible = adver_list[adversaire_index]
                    hero.attaque(ennemi_cible)
                    if ennemi_cible.ko is True:
                        adver_list.pop(ennemi_cible)
                else:
                    print("Index d'adversaire invalide.")
            except: pass
        elif choix == "2":
            print(f"{hero.nom} ne fait rien")
        elif choix == "3":
            try: hero.utiliser_objet(herbe1, hero)
            except: print("aucun objet")
        else:
            print("1 ou 2 comme choix possible")
            continue

        for i in adver_list:
            if not i.ko:
                choix_ennemi = randint(0, 5)
                if choix_ennemi < 4:
                    i.attaque(hero)
                if choix_ennemi >= 4:
                    print(f"{i.nom} ne fait rien")
                # Vérifier si le hero est ko
                if hero.ko is True: return

        for ennemi in ennemy:
            if ennemi.ko:
                if ennemi not in perso_ko:
                    perso_ko.append(ennemi)
        # Retirer les ennemis KO de la liste
        nouvelle_adver_list = []  # Initialiser une nouvelle liste pour les ennemis restants
        for ennemi in adver_list:  # Parcourir chaque ennemi dans adver_list
            if not ennemi.ko:  # Si l'ennemi n'est pas KO, l'ajouter à la nouvelle liste
                nouvelle_adver_list.append(ennemi)
        adver_list = nouvelle_adver_list  # Remplacer adver_list par la nouvelle liste filtrée
        if len(perso_ko) > 0:
            print(("=" * 10) + "KO" + ("=" * 10))
            for i in perso_ko:
                print(f"{i.nom}, exp {i.valeur_exp}")
            print("=" * 20)