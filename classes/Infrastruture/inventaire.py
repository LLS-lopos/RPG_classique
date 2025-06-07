from classes.Infrastruture.comptenue_jeu import Dictionnaire


class Inventaire(Dictionnaire):
    def __init__(self):
        super().__init__()
        self.dictmaison = {}

    def deposer_element(self, cle, valeur):
        self.dictmaison[cle] = valeur
        print(f"Vous déposez {valeur}.")

    def recuperer_element(self, cle, cible):
        if cle in self.dictmaison:
            cible.ajouter_element(cle, self.dictmaison[cle])
            del self.dictmaison[cle]
            print(f"Vous récupérez {cle}.")
        else:
            print(f"{cle} n'est pas dans votre maison.")