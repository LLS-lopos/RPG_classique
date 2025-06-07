from random import randint

from fonction_mod.affichage_texte import affichage_texte
from fonction_mod.list_menu import menu_combat, perso_vivant, perso_ko
from fonction_mod.F_liste_comparaison import equipe_grand_vers_petit, equipe_petit_vers_grand


def combat(g_hero: list, g_ennemy: list):
    while True:
        # Déterminer l'ordre des tours pour ce combat en fonction de la vitesse des personnages
        perso_vivant = equipe_grand_vers_petit(g_hero, g_ennemy)
        print("combat", perso_vivant)

        # ... (Le reste de votre logique de combat utilisera 'final_turn_order') ...
        choix = input(">>> ")
        if choix == "1":
            continue
        else:
            break
    
if __name__ == "__main__":
    combat()