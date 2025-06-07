from classes.Infrastruture.inventaire import Inventaire


class Sac(Inventaire):
    def __init__(self, capacite):
        super().__init__()
        self.capacite = capacite
        self.contenue = {}

    def ajouter_element(self, cle, valeur):
        if len(self.contenue) < self.capacite:
            self.contenue[cle] = valeur
            print(f"Vous ajoutez {valeur} dans votre sac.")
        else:
            print("Le sac est plein.")

    def supprimer_element(self, cle):
        if cle in self.contenue:
            del self.contenue[cle]
            print(f"{cle} a été retiré de votre sac.")
        else:
            print("Cet objet n'est pas dans votre sac.")