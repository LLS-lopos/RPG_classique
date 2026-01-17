from FermeFarming.jeuFF import farming_ferme
from RPG_Assembly.assembly import jeu_assembly
from classes.personnage.monstre.p_splip import Splip
from classes.objet.classique.herbe import HerbeMedicinal1
from classes.personnage.perso import Personnage
from fonction_mod.combat.FM_groupe_ennemi import groups_ennemi
from fonction_mod.combat.M_combat_equipe import combat
from fonction_mod.combat.M_combat_simple import combat_simple
from fonction_mod.combat.M_combat_un_contre_group import combat_un_contre_group
from interface.interface.affichage_texte import affichage_texte
from interface.interface.list_menu import accueil, mode
from MiniJeuxCookies.jeuMJC import game_cookie


def boucle_de_jeu():
    affichage_texte("RPG GAME", "RPG ADVENTURE CLASSIQUE CLI", "v0.1")
    while True:
        affichage_texte(accueil, "Accueil")
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
        hero = Personnage("XANA", 60, 0, 3, 4)
        ins_splip = Splip(att=6)
        group1 = groups_ennemi(10)
        affichage_texte(mode, " Mode de Jeu ")
        mode_de_jeu = input("-> ")
        if mode_de_jeu == "1":
            combat_simple(hero, ins_splip)
        elif mode_de_jeu == "2":
            combat_un_contre_group(hero, group1)
        elif mode_de_jeu == "3":
            combat([hero], group1)
        elif mode_de_jeu == "4":
            game_cookie()
        elif mode_de_jeu == "5":
            farming_ferme()
        elif mode_de_jeu == "6":
            jeu_assembly()
        elif mode_de_jeu == "7": break
        else: continue

def test():
    herbe1 = HerbeMedicinal1()
    print(f"Instance {herbe1}")
    hero = Personnage("XANA", 60, 0, 3, 4)
    ins_splip = Splip(att=6)
    hero.__repr__()
    hero.remplir_sac(herbe1, 1)
    hero.remplir_sac(herbe1, 1)
    hero.remplir_sac(herbe1, 4)
    ins_splip.attaque(hero)
    ins_splip.attaque(hero)
    ins_splip.attaque(hero)
    hero.voir_contenue_sac()
    hero.utiliser_objet(herbe1, hero)

    hero.voir_contenue_sac()
    hero.__repr__()

if __name__ == '__main__':
    boucle_de_jeu()
