from RPG_Assembly.classe.personnages.hero.p_class.Player import Joueur
from RPG_Assembly.fonction.generer_ennemie import generation_ennemie
from fonction_mod.utile.F_compteur_tour import compteur_tour
from interface.interface.affichage_texte import affichage_texte


def combat():
    #####################################
    # la fonction gère chaque combat
    # gère les tours
    # demande les actions au joueur
    # fait jouer l’ennemi
    # s’arrête quand l’un des deux meurt
    #####################################
    group_ennemi = generation_ennemie(4)
    ludo = Joueur()
    group_hero = [ludo]
    start = True
    tour = 0
    while start:
        acteur = group_hero + group_ennemi
        print(60*"=")
        tour = compteur_tour(tour)
        affichage_texte("Combat", "Assembly", f"Tour: {tour}")
        affichage_texte(acteur, "Liste Personnage")
        affichage_texte(["1 attaque", "2 magie", "3 fuite"], "Action", "Que Faire ?")
        choix = input(">>> ")
        # définir une cible pour les héros
        for h in group_hero:
            h.choix_cible(group_ennemi)
        # définir une cible pour les ennemies
        for e in group_ennemi:
            e.choix_cible(group_hero)
        # jouer
        for i in acteur:
            # choisir une cible
            if i.vivant:
                i.jouer(choix)
                # vérifie si des personnages sont KO
                for i in group_ennemi[:]:
                    if not i.vivant:
                        i.ko()
                        group_ennemi.remove(i)
                for i in group_hero[:]:
                    if not i.vivant:
                        i.ko()
                        group_hero.remove(i)

        if not group_ennemi:
            affichage_texte("Vous avez vaincu tous vos adversaire", "Victoire", "Fin de l'affrontement")
            break
        if not group_hero:
            affichage_texte("Vous avez perdu", "Défaite", "Fin de l'affrontement")
            break