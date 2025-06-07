class Dictionnaire:
    def __init__(self):
        self.dictionnaire = {}

    def ajouter_element(self, cle, valeur):
        self.dictionnaire[cle] = valeur

    def supprimer_element(self, cle):
        del self.dictionnaire[cle]

    def afficher_dictionnaire(self):
        print(self.dictionnaire)