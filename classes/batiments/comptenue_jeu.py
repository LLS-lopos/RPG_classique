class Dictionnaire:
    def __init__(self):
        self.dictionnaire = {}

    def ajouter_element(self, cle, valeur):
        print(cle.nom, cle, valeur)
        self.dictionnaire[cle.nom] = [cle, valeur]
        print(f"{self.dictionnaire[cle]} à été ajouté")

    def supprimer_element(self, cle):
        del self.dictionnaire[cle]
        print(f"{cle} à été suprimé")

    def afficher_dictionnaire(self):
        for cle, valeur in enumerate(self.dictionnaire):
            print(cle, valeur, self.dictionnaire[valeur])