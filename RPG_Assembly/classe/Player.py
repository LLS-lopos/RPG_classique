from RPG_Assembly.classe.perso import Personnage


class Joueur(Personnage):
    def __init__(self, nom="Joueur", pv=20, att=3):
        super().__init__(nom, pv, att)