from RPG_Assembly.classe.magie.sort import Sort


class Sort_soin(Sort):
    def __init__(self, nom: str, cout_pm: int, soin: int):
        super().__init__(nom, cout_pm)
        self._nom = nom
        self._cout_pm = cout_pm
        self._soin = soin

    def soigner(self, lanceur):
        if lanceur._pm >= self._cout_pm:
            lanceur._pm -= self._cout_pm
            return self._soin
        else:
            return False