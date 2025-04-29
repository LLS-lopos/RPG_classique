from classes.perso import personnage


class Guerrier(personnage):
    def __init__(self, nom: str="guerrier", pv: int=20, att: int=8, ko: bool=False, val_exp: int=6):
        personnage.__init__(self, nom, pv, att, ko)
        self.nom = nom
        self.pv = pv
        self.att = att
        self.ko = ko
        self.valeur_exp = val_exp

        self.exp = 0
        self.exp_max = 100
        self.niv = 0
        self.niv_max = 20