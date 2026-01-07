from classes.batiments.comptenue_jeu import Dictionnaire


class Inventaire(Dictionnaire):
    def __init__(self):
        super().__init__()

    def deposer_element(self, cle, valeur):
        self.dictionnaire[cle] = valeur
        print(f"Vous déposez {valeur}.")

    def recuperer_element(self, cle, cible):
        if cle in self.dictionnaire:
            cible.ajouter_element(cle, self.dictionnaire[cle])
            del self.dictionnaire[cle]
            print(f"Vous récupérez {cle}.")
        else:
            print(f"{cle} n'est pas dans votre maison.")