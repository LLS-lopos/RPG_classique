from random import randint


class personnage:
    def __init__(self, nom: str, pv: int, att: int, ko: bool=False, val_exp: int=3):
        super().__init__()
        self.nom = nom
        self.pv = pv
        self.att = att
        self.ko = ko
        self.valeur_exp = val_exp

        self.exp = 0
        self.exp_max = 100
        self.niv = 0
        self.niv_max = 20

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
            old_exp_max = self.exp_max
            old_val_exp = self.valeur_exp
            self.niv += 1
            self.exp = 0
            self.exp_max += randint(50, 200)
            self.valeur_exp += randint(4, 12)
            print(
                f"{self.nom} gagne un niveau"
                f"\nNIVEAU      : {old_niv} --> {self.niv}"
                f"\nEXP MAX     : {old_exp_max} --> {self.exp_max}"
                f"\nVALEUR EXP  : {old_val_exp} --> {self.valeur_exp}"
            )

            n_niveau -= 1

    def __str__(self):
        return self.nom, self.pv, self.att, self.ko

