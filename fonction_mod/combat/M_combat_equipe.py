from interface.interface.affichage_texte import affichage_texte
from interface.interface.list_menu import menu_combat
from fonction_mod.utile.F_liste_comparaison import equipe_grand_vers_petit


def combat(g_hero: list, g_ennemy: list):
    # Déterminer l'ordre des tours pour ce combat en fonction de la vitesse des personnages
    perso_vivant = equipe_grand_vers_petit(g_hero, g_ennemy)
    nom_perso = []
    for i in perso_vivant:
        nom_perso.append(i.nom)
    affichage_texte(msg=nom_perso, titre="tour")
    affichage_texte(menu_combat, " Action ")
    while True:
        choix = input("-> ")
        if choix == "1":
            continue
        else:
            break
    
if __name__ == "__main__":
    combat()