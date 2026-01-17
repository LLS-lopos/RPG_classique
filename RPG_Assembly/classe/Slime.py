from RPG_Assembly.classe.perso import Personnage


class Slime(Personnage):
    def __init__(self, nom="slime", pv=5, att=2):
        super().__init__(nom, pv, att)