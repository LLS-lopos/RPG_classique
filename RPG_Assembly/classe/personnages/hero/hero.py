from RPG_Assembly.classe.magie.offensif.feu.flame import Flame
from RPG_Assembly.classe.personnages.perso import Personnage
from interface.interface.affichage_texte import affichage_texte


class Hero(Personnage):
    def __init__(self, nom, pv, pm, att, vivant, cible, arme1):
        super().__init__(nom, pv, pm, att, vivant, cible, arme1)

    def jouer(self, commande):
        if commande == "1":
            self.attaquer(self._cible)
        elif commande == "2":
            self.magie()
        elif commande == "3":
            pass

    def magie(self):
        m_flame = Flame()
        if m_flame:
            affichage_texte(f"Lance le sort {m_flame._nom}", self._nom, m_flame._element)
            self._cible.recevoir_degat(m_flame._degat)

