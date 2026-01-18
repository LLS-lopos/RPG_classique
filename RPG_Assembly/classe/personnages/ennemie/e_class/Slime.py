from RPG_Assembly.classe.personnages.ennemie.ia_ennemie import Ennemie


class Slime(Ennemie):
    def __init__(self, nom="slime", pv=5, att=2, vivant=True, cible=None, arme1=None):
        super().__init__(nom, pv, att, vivant, cible, arme1)