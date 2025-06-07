from classes.objet.objet import Objet


class HerbeMedicinal1(Objet):
    def __init__(self, nom="herbe médicinal", categorie="soin", prix=5, valeur=20, description="Herbe médicinal qui permet de récupérer 20 PV"):
        Objet.__init__(self, nom, categorie, prix, valeur, description)
        self.nom = nom
        self.categarie = categorie
        self.prix = prix
        self.valeur = valeur

    def utiliser(self, cible):
        #old = cible.pv
        cible.pv += self.valeur
        #dif_pv = cible.pv - old
        print(f"{cible.nom} utilise {self.nom} et récupère {"dif_pv"} PV")