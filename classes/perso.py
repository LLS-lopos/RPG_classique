import random
from random import randint, uniform
from classes.objet.classique.herbe import HerbeMedicinal1
from fonction_mod.F_mathematique import arrondir_entier_superieur


class Personnage:
    def __init__(self, nom: str, pv: int, att: int, vit: int, ko: bool=False, val_exp: int=3):
        super().__init__()
        self.nom = nom
        self.pv = pv
        self.pv_max = pv
        self.att = att
        self.vit = vit
        self.ko = ko
        self.valeur_exp = val_exp

        self.exp = 0
        self.exp_max = 100
        self.niv = 0
        self.niv_max = 20

        self.sac = []
        self.capaciter_max = 10

        self.equipement = {
            "arme principal": None,  # arme lourde
            "arme secondaire": None,  # arme légère
            "bouclier": None,  # armurerie
            "chapeau": None,  # Vêtement/armurerie
            "vet_haut": None,  # Vêtement/armurerie
            "vet_bas": None,  # Vêtement/armurerie
            "gant": None,  # Vêtement/armurerie
            "chaussure": None,  # Vêtement/armurerie
            "accesoire primaire": None,  # bague/bracelet/collier/anneaux/amulette
            "accesoire secondaire": None,  # bague/bracelet/collier/anneaux/amulette
            "sac": None,  # sac à dos pour l'inventaire
        }

    def attaque(self, cible):
        cible.pv -= self.att
        print(f"{self.nom} attaque {cible.nom}")
        if cible.pv <= 0:
            cible.pv = 0
            cible.ko = True
        print(f"{cible.nom} perd {self.att} PV, il lui reste {"💚"*cible.pv} PV")
        if cible.ko is True:
            cible.mort()
            print(f"{self.nom} gagne {cible.valeur_exp} point d'expérience")
            self.gain_exp(cible.valeur_exp)

    def mort(self):
        if self.ko:
            print(f"{self.nom} est KO et ne peut plus ce battre\n")

    def gain_exp(self, gain_exp):
        if self.niv < self.niv_max:
            self.exp += gain_exp
            while True:
                if self.exp >= self.exp_max:
                    if self.niv < self.niv_max:
                        reste = self.exp - self.exp_max
                        self.niveau_sup()
                        self.exp += reste
                        reste = 0
                        if self.exp > self.exp_max: continue
                        else: break
                    else:
                        self.exp = 0
                        print(f"{self.nom} est à son niveau maximum")
                        break
                else: break
            print(f"{self.nom} a {self.exp} exp")
        else: print("Niveau maximum atteint")

    def niveau_sup(self, n_niveau=None):
        if n_niveau is None:
            n_niveau = 1
        while n_niveau:
            old_niv = self.niv
            old_att = self.att
            old_vit = self.vit
            old_exp_max = self.exp_max
            old_val_exp = self.valeur_exp
            self.niv += 1
            self.exp = 0
            self.exp_max *= random.uniform(1.2, 1.6)
            arrondir_entier_superieur(self.exp_max)
            self.exp_max = int(self.exp_max)
            self.valeur_exp += randint(4, 12)
            self.att += randint(0, 5)
            self.vit += randint(0, 4)
            print(
                f"{self.nom} gagne un niveau"
                f"\nNIVEAU      : {old_niv} --> {self.niv}"
                f"\nATTAQUE     : {old_att} --> {self.att}"
                f"\nVITESSE     : {old_vit} --> {self.vit}"
                f"\nEXP MAX     : {old_exp_max} --> {self.exp_max}"
                f"\nVALEUR EXP  : {old_val_exp} --> {self.valeur_exp}"
            )
            n_niveau -= 1

    def remplir_sac(self, objet, capaciter=0):
        capaciter = len(self.sac)
        if capaciter < self.capaciter_max:
            self.sac.append(objet.nom)
            capaciter += 1
            print(f"{objet.nom} à été ajouter à l'inventaire\nplace utiliser {capaciter}/{self.capaciter_max}")
        else:
            print("Ton sac est plein")

    def utiliser_objet(self, objet, cible):
        if objet in self.sac:
            print("ok")
            objet.utiliser(cible)
            self.sac.pop(objet)

    def voir_contenue_sac(self):
        print("#### Objet dans le sac ####")
        for i in self.sac:
            print(i)
        print("###########################")

    def __repr__(self):
        return f"{self.nom}, {self.pv}, {self.att}, {self.vit}, {self.ko}"
