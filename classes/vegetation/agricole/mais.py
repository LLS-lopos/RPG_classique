from classes.vegetation.vegetation import vegetation


class Mais(vegetation):
    def __init__(self, nom="Maïs", init_temps=0, vit_pousse=2, prix=3):
        super().__init__(nom, init_temps, vit_pousse)
        self._prix = prix

    def vendre(self):
        return self._prix