from classes.Infrastruture.comptenue_jeu import Dictionnaire


class Boutique(Dictionnaire):
    def __init__(self):
        super().__init__()
        self.pieces = 0

    def acheter_element(self, cle, valeur, prix):
        if self.pieces >= prix:
            self.ajouter_element(cle, valeur)
            self.pieces -= prix
            print(f"{cle} acheté pour {prix} pièces.")
        else:
            print("Vous n'avez pas assez de pièces pour acheter cet objet.")

    def vendre_element(self, cle, prix):
        if cle in self.dictionnaire:
            self.supprimer_element(cle)
            self.pieces += prix
            print(f"{cle} vendu pour {prix} pièces.")
        else:
            print("Vous ne possédez pas cet objet.")