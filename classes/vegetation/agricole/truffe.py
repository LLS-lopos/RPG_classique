from classes.vegetation.vegetation import vegetation


class Truffe(vegetation):
    def __init__(self, nom="Truffe", init_temps=0, vit_pousse=20, prix=20):
        super().__init__(nom, init_temps, vit_pousse)
        self._prix = prix

    def vendre(self):
        return self._prix