from RPG_Assembly.classe.magie.sort import Sort


class SortATT(Sort):
    def __init__(self, nom: str, cout_pm: int, degat: int):
        super().__init__(nom, cout_pm)
        self._nom = nom
        self._cout_pm = cout_pm
        self._degat = degat

    def offensive(self, lanceur):
        if lanceur._pm >= self._cout_pm:
            lanceur._pm -= self._cout_pm
            return self._degat
        else:
            return False
