class Arme:
    def __init__(self, nom: str, att: int):
        super().__init__()
        self._nom = nom
        self._attaque = att

    def sup_attaque(self):
        return self._attaque