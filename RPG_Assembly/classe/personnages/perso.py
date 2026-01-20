from interface.interface.affichage_texte import affichage_texte


class Personnage:
    def __init__(self, nom: str, pv: int, pm: int, att: int, vivant: bool, cible=None, arme1=None):
        super().__init__()
        self._nom = nom
        self._pv = pv
        self._pm = pm
        self._attaque = att
        self._vivant = vivant
        self._cible = cible

        self._arme1 = arme1

        self._action = ["1 attaquer", "2 sort", "3 fuire"]
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

    def attaquer(self, cible):
        affichage_texte("attaque", self.nom, cible.nom)
        cible.recevoir_degat(self._att)

    def recevoir_degat(self, degat):
        affichage_texte(f"subit {degat} point de dégât", self.nom, "dégât reçu")
        self._pv -= degat
        if self._pv <= 0:
            self._pv = 0
            self._vivant = False
        else:
            print(f"{self.nom} à encore {self._pv} PV")

    def __str__(self):
        return f"{self.nom}: {self._pv} PV, {self._att} ATT, {self._pm} PM"

    def ko(self):
        return affichage_texte("N'a Plus de PV", self.nom, "KO")

    @property
    def vivant(self):
        return self._vivant

    @property
    def nom(self):
        return self._nom