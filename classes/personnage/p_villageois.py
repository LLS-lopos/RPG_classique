from classes.perso import Personnage


class Villageois(Personnage):
    def __init__(self, nom: str="villageois", pv: int=10, att: int=2, ko: bool=False, val_exp: int=1):
        Personnage.__init__(self, nom, pv, att, ko)
        self.nom = nom
        self.pv = pv
        self.att = att
        self.ko = ko
        self.valeur_exp = val_exp

        self.exp = 0
        self.exp_max = 100
        self.niv = 0
        self.niv_max = 20