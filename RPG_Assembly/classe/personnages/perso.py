from interface.interface.affichage_texte import affichage_texte


class Personnage:
    def __init__(self, nom: str, pv: int, att: int, vivant: bool, cible=None, arme1=None):
        super().__init__()
        self._nom = nom
        self._pv = pv
        self._attaque = att
        self._vivant = vivant
        self._cible = cible

        self._arme1 = arme1

        self._action = ["1 attaquer", "2 fuire"]
        if self._arme1 is not None:
            self._att = self._attaque + self._arme1.sup_attaque()
        else:
            self._att = self._attaque

    def choix_cible(self, groupe: list):
        if len(groupe) == 1:
            self._cible = groupe[0]
        else:
            affichage_texte(groupe, "Choisir Cible")
            choix = input(">>> ")
            self._cible = groupe[choix.isdigit()]
        return self._cible

    def vivant(self):
        return self._vivant

    def attaquer(self, cible):
        print(f"{self._nom} attaque {cible._nom}")
        cible.recevoir_degat(self._att)

    def recevoir_degat(self, degat):
        print(f"{self._nom} subit {degat} point de dégât")
        self._pv -= degat
        if self._pv <= 0:
            self._pv = 0
            self._vivant = False
        else:
            print(f"{self._nom} à encore {self._pv} PV")

    def KO(self):
        return affichage_texte("N'a Plus de PV", self._nom, "KO")

    def __str__(self):
        return f"{self._nom}: {self._pv} PV, {self._att} ATT"

    @property
    def nom(self):
        return self._nom