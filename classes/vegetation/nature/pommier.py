import random

from classes.vegetation.agricole.pomme import Pomme
from classes.vegetation.vegetation import vegetation


class Pommier(vegetation):
    def __init__(self, nom="Pommier", init_temps=0, vit_pousse=7, cueillir=False, tempo=False, temporiser=0, fruit="Pomme"):
        super().__init__(nom, init_temps, vit_pousse, cueillir)
        self._fruit = fruit
        self._tempo = tempo
        self._temporiser = temporiser
        self._tempo_max = vit_pousse*2

    def check_mure(self):
        tempo = self.temporiser()
        if tempo == False:
            if not self._mure:
                self._init_temps += 1
                if self._init_temps == self._vit_pousse:
                    self._mure = True
            else:
                self._mure = False
                self._tempo = True
                self._init_temps = 0


    def pousse_fruit(self):
        if self._mure == True and self._cueillir == False:
            self.apparition_pomme()
            self._cueillir = True

    def apparition_pomme(self):
        a = random.randint(5, 20)
        return a

    def temporiser(self):
        if self._tempo == True:
            if self._temporiser != self._tempo_max:
                self._temporiser += 1
            else:
                self._temporiser = 0
                self._init_temps = 0
                self._tempo = False
            return True
        else:
            return False

    def __str__(self):
        etat = ''
        if self._mure:
            etat = " [mure]"
        return f"{self._nom} ({self._init_temps}/{self._vit_pousse}){etat} [{self._temporiser}/{self._tempo_max}]"

    def __repr__(self):
        etat = ''
        if self._mure:
            etat = " [mure]"
        return f"{self._nom} ({self._init_temps}/{self._vit_pousse}){etat} [{self._temporiser}/{self._tempo_max}]"