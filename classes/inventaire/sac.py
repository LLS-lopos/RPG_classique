from classes.batiments.comptenue_jeu import Dictionnaire


class Sac(Dictionnaire):
    def __init__(self, n_objet, n_copie):
        super().__init__()
        self.copie = n_copie
        self.nombre_obj = n_objet

    def ajouter_element(self, cle, valeur):
        print(cle.nom, cle, valeur)
        if len(self.dictionnaire) < self.nombre_obj:
            if cle.nom in self.dictionnaire:
                print(f"{cle.nom} existe déjà dans le sac\nil y en à {self.dictionnaire[cle.nom][-1]} exemplaire")
                for num in range(valeur):
                    if self.dictionnaire[cle.nom][-1] < self.copie:
                        self.dictionnaire[cle.nom][-1] +=1
                    else:
                        print(f"Le nombre maximum d'exemple de {cle} est atteint")
            else:
                self.dictionnaire[cle.nom] = [cle, valeur]
                if self.dictionnaire[cle.nom][1] > self.copie:
                    self.dictionnaire[cle.nom][1] = self.copie
            print(f"Vous ajoutez {valeur} dans votre sac.")
        else:
            print("Le sac est plein.")
        print(self.dictionnaire)
        print(self.copie)
        print(self.nombre_obj)

    def retirer_element(self, cle):
        print(f"VOIR: {cle}")
        if cle in self.dictionnaire:
            if self.dictionnaire[cle][1] > 0:
                self.dictionnaire[cle][1] -= 1
            if self.dictionnaire[cle][1] == 0:
                self.supprimer_element(cle)
        else:
            print("Cet objet n'est pas dans votre sac.")
            return

    def voir_comptenue(self):
        print(self.dictionnaire)