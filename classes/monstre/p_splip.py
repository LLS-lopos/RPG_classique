from random import randint
from classes.perso import Personnage


class Splip(Personnage):
    def __init__(self, nom: str="splip", pv: int=6, pm=3, att: int=2, vit: int=3, ko: bool=False, val_exp: int=10):
        Personnage.__init__(self, nom, pv, pm, att, ko)
        self.nom = nom
        self.pv = pv
        self.pm = pm
        self.att = att
        self.vit =vit
        self.ko = ko
        self.valeur_exp = val_exp

        self.pv_max = pv
        self.pm_max = pm

        self.exp = 0
        self.exp_max = 100
        self.niv = 0
        self.niv_max = 20