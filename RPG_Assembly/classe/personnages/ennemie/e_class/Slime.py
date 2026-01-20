from RPG_Assembly.classe.magie.medical.soin.premier_secours import PremierSecours
from RPG_Assembly.classe.personnages.ennemie.ia_ennemie import Ennemie


class Slime(Ennemie):
    def __init__(self, nom="slime", pv=7, pm=9, att=2, vivant=True, cible=None, arme1=None):
        super().__init__(nom, pv, pm, att, vivant, cible, arme1)
        self._max_pv = pv
        self._max_pm = pm

    def jouer(self, commande=None):
        if self._pm >= self._max_pm*0.25 and self._pv <= self._max_pv*0.25:
            self.m_soin()
        elif self._cible:
            self.attaquer(self._cible)

    def m_soin(self):
        p_soin = PremierSecours()
        if p_soin:
            self._pv += p_soin.soigner(self)
            if self._pv > self._max_pv:
                self._pv = self._max_pv
            print(f"{self._nom} utilise {p_soin._nom}")
