from classes.objet.objet import Objet


class HerbeMedicinal1(Objet):
    def __init__(self, nom="herbe médicinal", categorie="soin", prix=5, valeur=20, description="Herbe médicinal qui permet de récupérer 20 PV"):
        Objet.__init__(self, nom, categorie, prix, valeur, description)
        self.nom = nom
        self.categarie = categorie
        self.prix = prix
        self.valeur = valeur

