from random import randint

from classes.personnage.villageois.p_villageois import Villageois


class Mamie(Villageois):
    def __init__(self, nom: str="mamie", niveau=1, basse_cookie=1, retraiter=False):
        Villageois.__init__(self, nom, niveau, basse_cookie, retraiter)
        self._nom = nom
        self._niv = niveau
        self._cui_cookie = basse_cookie
        self._production = 0
        self._production_max = 40
        self._retraiter = retraiter

    def cookie_produit(self):
        print(f"{self._nom} à préparer {self._cui_cookie} cookie, ({self._production + self._cui_cookie})")
        self._production += self._cui_cookie
        if self._production == 10:
            self.niv_suivant()
        elif self._production in [20, 21, 22]:
            self.niv_suivant()
        return self._cui_cookie

    def niv_suivant(self):
        val = randint(1, 3)
        self._cui_cookie += val
        self._niv += 1
        print(f"{self._nom} monte de niveau:\n\tNiv : {self._niv-1} -> {self._niv}\n\tProd: {self._cui_cookie-val} -> {self._cui_cookie}")

    def retraite(self):
        if self._production >= self._production_max:
            print(f"Après avoir produit {self._production} cookies, {self._nom} prend maintenant sa retraite")
            self._retraiter = True
            return True
        return False

    def __str__(self):
        return f"Nom: {self._nom}, production cookie: {self._cui_cookie}, Niveau: {self._niv}, nombre de cookie: {self._production}, retraite: {self._retraiter}"

    def __repr__(self):
        return f"Nom: {self._nom}, production cookie: {self._cui_cookie}, Niveau: {self._niv}, nombre de cookie: {self._production}, retraite: {self._retraiter}"

    def __eq__(self, other):
        return self._nom == other._nom and self._niv == other._niv