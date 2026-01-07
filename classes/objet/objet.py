class Objet:
    def __init__(self, nom: str, categorie: str, prix: int, valeur, description):
        super().__init__()
        self.nom = nom
        self.categarie = categorie
        self.prix = prix
        self.valeur = valeur
        self.description = description

    def utiliser(self, cible):
        old = cible.pv
        cible.pv += self.valeur
        if cible.pv > cible.pv_max:
            cible.pv = cible.pv_max
        dif_pv = old - cible.pv
        print(f"{cible.nom} utilise {self.nom} et récupère {dif_pv} PV")