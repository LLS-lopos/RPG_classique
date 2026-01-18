from RPG_Assembly.classe.personnages.perso import Personnage


class Ennemie(Personnage):
    def __init__(self, nom, pv, att, vivant, cible, arme1):
        super().__init__(nom, pv, att, vivant, cible, arme1)

    def jouer(self):
        if self._cible:
            self.attaquer(self._cible)