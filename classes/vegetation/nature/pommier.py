from classes.vegetation.vegetation import vegetation


class Pommier(vegetation):
    def __init__(self, nom="Pommier", init_temps=0, vit_pousse=3, fruit="Pomme"):
        super().__init__(nom, init_temps, vit_pousse)
        self._fruit = fruit

    def pousse_fruit(self):
        if self._mure == True:
            self.check_mure()