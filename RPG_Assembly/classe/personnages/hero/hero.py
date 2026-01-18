from RPG_Assembly.classe.personnages.perso import Personnage
from interface.interface.affichage_texte import affichage_texte


class Hero(Personnage):
    def __init__(self, nom, pv, att, vivant, cible, arme1):
        super().__init__(nom, pv, att, vivant, cible, arme1)

    def jouer(self):
        affichage_texte(self._action, "Action", "Que Faire ?")
        choix = input(">>> ")
        if choix == "1":
            self.attaquer(self._cible)
        elif choix == "2":
            pass
