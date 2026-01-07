from classes.objet.objet import Objet


class Bonbon(Objet):
    def __init__(self, nom="bonbon", categorie="soin", prix=5, valeur=3, description="sucrerie, récupérer 3 PV"):
        Objet.__init__(self, nom, categorie, prix, valeur, description)
        self.nom = nom
        self.categarie = categorie
        self.prix = prix
        self.valeur = valeur
