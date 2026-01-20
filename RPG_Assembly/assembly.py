# RPG Assembly
# Type rog-like au tour per tour
import sys

from RPG_Assembly.classe.personnages.hero.p_class.Player import Joueur
from RPG_Assembly.classe.personnages.ennemie.e_class.Slime import Slime
from RPG_Assembly.fonction.bonus import bonus
from RPG_Assembly.fonction.combat import combat
from RPG_Assembly.tk_assembly import GameUI
from fonction_mod.utile.F_compteur_tour import compteur_tour
from interface.interface.affichage_texte import affichage_texte


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


def assembly_game():
    affichage_texte(["1 Combat", "2 Quitter"], "Menu", "Assembly")
    choix = input(">>> ")
    if choix == "1":
        while True:
            combat()
            bonus()
            continuer = input("continuer o/n\n>>> ")
            if continuer == "o":
                continue
            else:
                break
    elif choix == "2":
        sys.exit()
    else:
        pass

if __name__ == "__main__":
    choix = input("CLI/GRAPHIC ?\n>>> ")
    if choix == "CLI":
        assembly_game()
    elif choix == "GRAPHIC":
        jeu_tk_assembly()
