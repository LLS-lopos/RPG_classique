class Personnage:
    def __init__(self, nom: str, pv: int, att: int):
        super().__init__()
        self._nom = nom
        self._pv = pv
        self._attaque = att

    def attaquer(self, cible):
        pass

    def recevoir_degat(self, lanceur):
        pass