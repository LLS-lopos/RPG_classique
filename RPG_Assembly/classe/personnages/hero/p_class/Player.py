from RPG_Assembly.classe.armes.epee.epee_bois import epee_bois
from RPG_Assembly.classe.personnages.hero.hero import Hero


class Joueur(Hero):
    def __init__(self, nom="Héro", pv=20, att=3, vivant=True, cible=None, arme1=epee_bois()):
        super().__init__(nom, pv, att, vivant, cible, arme1)