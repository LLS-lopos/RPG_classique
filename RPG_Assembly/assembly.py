# RPG Assembly
# Type rog-like au tour per tour
from RPG_Assembly.classe.Player import Joueur
from RPG_Assembly.classe.Slime import Slime
from fonction_mod.utile.F_compteur_tour import compteur_tour

joueur = Joueur()
glu = Slime()

def jeu_assembly():
    tour = 0
    while True:
        tour = compteur_tour(tour)
        choix = input("que faire ?\n>>> ")
        if choix == "1":
            print(joueur)
        elif choix == "2":
            print(glu)
        else:
            break


if __name__ == "__main__":
    jeu_assembly()