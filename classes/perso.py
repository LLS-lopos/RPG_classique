import json
import pathlib
from random import randint, uniform
from fonction_mod.utile.F_mathematique import arrondir_entier_superieur


class Personnage:
    def __init__(self, nom: str, pv: int, pm: int, att: int, vit: int, ko: bool=False, val_exp: int=3):
        super().__init__()
        self.nom = nom
        self.pv = pv
        self.pm = pm
        self.att = att
        self.vit = vit
        self.ko = ko
        self.valeur_exp = val_exp

        self.pv_max = pv
        self.pm_max = pm

        self.exp = 0
        self.exp_max = 100
        self.niv = 0
        self.niv_max = 30

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
            if self.niv >= self.niv_max:
                print(f"{self.nom} est déjà au niveau maximum" )
                return
            old_niv = self.niv
            old_att = self.att
            old_vit = self.vit
            old_exp_max = self.exp_max
            old_val_exp = self.valeur_exp
            old_pv_max = self.pv_max
            old_pm_max = self.pm_max
            self.niv += 1
            self.exp = 0
            self.exp_max *= uniform(1.1, 1.3)
            arrondir_entier_superieur(self.exp_max)
            self.exp_max = int(self.exp_max)
            self.valeur_exp += randint(2, 6)
            self.att += randint(0, 4)
            self.vit += randint(0, 3)
            self.pv_max += randint(0, 5)
            self.pm_max += randint(0, 2)
            print(
                f"{self.nom} gagne un niveau"
                f"\nNIVEAU      : {old_niv} --> {self.niv}"
                f"\nPV MAX      : {old_pv_max} --> {self.pv_max}"
                f"\nPM MAX      : {old_pm_max} --> {self.pm_max}"
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

    def sauvegarde(self):
        save_player = pathlib.Path.home() / ".RPG_CLASSIQUE" / ("player_" + str(self.nom) + ".json")
        if not save_player.exists():
            save_player.touch()
        doc_loc = {
            "niv": self.niv,
            "nom": self.nom,
            "pv": self.pv,
            "pm": self.pm,
            "att": self.att,
            "vit": self.vit,
            "ko": self.ko,
            "exp": self.exp,
            "pv max": self.pv_max,
            "pm max": self.pm_max,
            "exp max": self.exp_max,
            "niv max": self.niv_max,
            "valeur exp max": self.valeur_exp,
            "sac": self.sac,
            "capaciter sac": self.capaciter_max,
            "equipement": self.equipement,
        }
        with open(save_player, 'w', encoding="utf-8") as f:
            json.dump(doc_loc, f, indent=4)

    def charger(self):
        chager_player = pathlib.Path.home() / ".RPG_CLASSIQUE" / ("player_"+str(self.nom)+".json")
        if chager_player.exists():
            with open(chager_player, 'r', encoding="utf-8") as f:
                dico = json.load(f)
                for cle in dico:
                    if cle == "niv": self.niv = dico[cle]
                    if cle == "nom": self.nom = dico[cle]
                    if cle == "pv": self.pv = dico[cle]
                    if cle == "pm": self.pm = dico[cle]
                    if cle == "att": self.att = dico[cle]
                    if cle == "vit": self.vit = dico[cle]
                    if cle == "ko": self.ko = dico[cle]
                    if cle == "exp": self.exp = dico[cle]
                    if cle == "pv max": self.pv_max = dico[cle]
                    if cle == "pm max": self.pm_max = dico[cle]
                    if cle == "exp max": self.exp_max = dico[cle]
                    if cle == "niv max": self.niv_max = dico[cle]
                    if cle == "valeur exp max": self.valeur_exp = dico[cle]
                    if cle == "sac": self.sac = dico[cle]
                    if cle == "capaciter sac": self.capaciter_max = dico[cle]
                    if cle == "equipement": self.equipement = dico[cle]

    def __repr__(self):
        return (f"Niv : {self.niv}\n"
                f"Nom : {self.nom}\n"
                f"PV  : {self.pv}\n"
                f"ATT : {self.att}\n"
                f"VIT : {self.vit}\n"
                f"KO  : {self.ko}\n")

if __name__ == "__main__":
    ludo = Personnage("Ludo", 26, 0, 3, 4)
    print(ludo.__repr__())
    ludo.charger()
    print(ludo.__repr__())