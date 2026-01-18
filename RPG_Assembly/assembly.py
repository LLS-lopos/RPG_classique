# RPG Assembly
# Type rog-like au tour per tour
from RPG_Assembly.classe.personnages.hero.p_class.Player import Joueur
from RPG_Assembly.classe.personnages.ennemie.e_class.Slime import Slime
from RPG_Assembly.tk_assembly import GameUI
from fonction_mod.utile.F_compteur_tour import compteur_tour
from interface.interface.affichage_texte import affichage_texte


def jeu_assembly():
    acteur = []

    group_hero = []
    group_ennemi = []
    joueur = Joueur()
    for i in range(3):
        i = Slime()
        group_ennemi.append(i)
    group_hero.append(joueur)

    acteur += group_hero
    acteur += group_ennemi

    tour = 0
    start = True

    while start:
        tour = compteur_tour(tour)
        affichage_texte("Affrontement", "Assembly", f"Tour: {tour}")

        # définir une cible pour les héros
        for h in group_hero:
            h.choix_cible(group_ennemi)
        # définir une cible pour les ennemies
        for e in group_ennemi:
            e.choix_cible(group_hero)
        # jouer
        for i in acteur:
            # choisir une cible
            if i.vivant():
                i.jouer()
                # vérifie si des personnages sont KO
                for i in group_ennemi[:]:
                    if not i.vivant():
                        i.KO()
                        group_ennemi.remove(i)
                for i in group_hero[:]:
                    if not i.vivant():
                        i.KO()
                        group_hero.remove(i)
        if not group_ennemi:
            affichage_texte("Vous avez vaincu tous vos adversaire", "Victoire", "Fin de l'affrontement")
            break
        if not group_hero:
            affichage_texte("Vous avez perdu", "Défaite", "Fin de l'affrontement")
            break


def jeu_tk_assembly():
    ui = GameUI()

    acteur = []

    group_hero = []
    group_ennemi = []
    joueur = Joueur()
    """for i in range(3):
        i = Slime()
        group_ennemi.append(i)"""
    i = Slime()
    group_ennemi.append(i)
    group_hero.append(joueur)

    acteur += group_hero
    acteur += group_ennemi

    tour = 0
    start = True

    while start:
        tour = compteur_tour(tour)
        affichage_texte("Affrontement", "Assembly", f"Tour: {tour}")
        ui.set_player_stats(f"{group_hero[0].nom}\nPV: {group_hero[0]._pv}\nATT: {group_hero[0]._attaque}")
        ui.set_enemy_stats((f"{group_ennemi[0].nom}\nPV: {group_ennemi[0]._pv}\nATT: {group_ennemi[0]._attaque}"))


        # définir une cible pour les héros
        for h in group_hero:
            h.choix_cible(group_ennemi)
        # définir une cible pour les ennemies
        for e in group_ennemi:
            e.choix_cible(group_hero)

        ui.print(f"Affrontement\tAssembly\nTour: {tour}")
        choix = ui.input("1 : Attaquer\n2 : Fuite\nVotre choix : ")
        ui.print(f"Vous avez choisi : {choix}\n----------------")
        if choix == "1":
            group_hero[0].attaquer(group_ennemi[0])
            ui.print(f"{group_hero[0]._nom} attaque {group_ennemi[0]._nom}")
            ui.print(f"{group_ennemi[0]._nom} perd {group_hero[0]._attaque} point de dégât")
        elif choix == "2":
            ui.print("Vous prenez la fuite")
            break
        else:
            pass
        group_ennemi[0].attaquer(group_hero[0])
        ui.print(f"{group_ennemi[0]._nom} attaque {group_hero[0]._nom}")
        ui.print(f"{group_hero[0]._nom} perd {group_ennemi[0]._attaque} point de dégât")
        ui.print("================")

        ui.set_player_stats(f"{group_hero[0].nom}\nPV: {group_hero[0]._pv}\nATT: {group_hero[0]._attaque}")
        ui.set_enemy_stats((f"{group_ennemi[0].nom}\nPV: {group_ennemi[0]._pv}\nATT: {group_ennemi[0]._attaque}"))

        if not group_ennemi[0].vivant():
            ui.print(f"Victoire\nVous avez vaincu tous vos adversaire\nFin de l'affrontement")
            break
        if not group_hero[0].vivant():
            ui.print(f"Défaite\nVous avez perdu\nFin de l'affrontement")
            break



if __name__ == "__main__":
    choix = input("CLI/GRAPHIC ?\n>>> ")
    if choix == "CLI":
        jeu_assembly()
    elif choix == "GRAPHIC":
        jeu_tk_assembly()