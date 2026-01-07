from classes.objet.classique.herbe import HerbeMedicinal1

accueil = ["1 Jouer", "2 Info", "3 Test", "4 Quitter"]
mode = ["1 simple", "2 1vs_groupe", "3 equipe", "4 retour accueil"]

# en combat
menu_combat = ["1 attaque", "2 defence", "3 objet", "4 fuite"]
perso_vivant = []
perso_ko = []

# boutique
menu_boutique = ["acheter", "vendre"]
boutique_obj_n1 = {  # dans chaque catégorie -→ objets : class objet (nom, prix, valeur(effet), description)
    "objet" : {
        "herbe médicinal": HerbeMedicinal1(),
        "sandwitch": 12,
    },
    "armes": {
        "épée de bois": 6,
        "épée de cuivre": 15,
        "épée de fer": 32,
    },
    "vêtement": {},
}