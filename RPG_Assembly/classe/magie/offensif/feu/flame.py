from RPG_Assembly.classe.magie.offensif.sort_att import SortATT


class Flame(SortATT):
    def __init__(self, nom="flame", cout_pm=5, degat=8, element="FEU"):
        super().__init__(nom, cout_pm, degat)
        self._element = element