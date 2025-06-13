def grand_vers_petit(liste: list):
    sortie = []
    liste_cp = liste.copy()
    while liste_cp:
        if len(liste_cp) > 0:
            maxi = max(liste_cp)
            sortie.append(maxi)
            liste_cp.remove(maxi)
    return sortie

def petit_vers_grand(liste: list):
    sortie = []
    liste_cp = liste.copy()
    while liste_cp:
        if len(liste_cp) > 0:
            mini = min(liste_cp)
            sortie.append(mini)
            liste_cp.remove(mini)
    return sortie

def equipe_grand_vers_petit(a: list, b: list):
    liste_element = a + b
    perso_vivant = []
    perso_exeption = []

    for perso in liste_element:
        # 'perso' doit être un objet personnage avec un attribut 'vit' (vitesse)
        if hasattr(perso, 'vit'):
            perso_vivant.append([perso.vit, perso])
        else: # Gérer les cas où un combattant n'a pas d'attribut 'vit' (par exemple, enregistrer ou sauter)
            perso_exeption.append(perso)

    liste_vitesse = []
    for info in perso_vivant: liste_vitesse.append(info[0])  # Extraire uniquement les vitesses pour le tri
    # Trier les vitesses du plus grand au plus petit en utilisant la fonction importée
    reajust_liste_vitesse = grand_vers_petit(liste_vitesse)
    # Reconstruire la liste des personnages dans l'ordre de reajust_liste_vitesse
    ordre_de_tour = []
    # Utiliser une copie de perso_vivant pour permettre la suppression des éléments, gérant correctement les vitesses identiques
    ajust_par_vitesse = [info for info in perso_vivant] # Create a shallow copy
                                                                
    for vitesse in reajust_liste_vitesse:
        for index, info in enumerate(ajust_par_vitesse):
            if info[0] == vitesse:
                ordre_de_tour.append(info[1]) # Add the character object
                ajust_par_vitesse.pop(index) # Remove from copy to handle duplicates correctly
                break # Found character for this vitesse, move to next vitesse
    ordre_de_tour += perso_exeption
    
    # Maintenant, 'ordre_de_tour' contient les objets personnages triés par vitesse (décroissante).
    # Vous pouvez utiliser cette liste pour la séquence de combat.
    # Exemple : Afficher l'ordre des tours
    #print("\nOrdre des tours (par vitesse décroissante):")
    for tourPerso in ordre_de_tour:
        nom_perso = getattr(tourPerso, 'nom', 'Personnage inconnu')  # On récupère l'attribut 'nom' des classes/sous_classe 'perso' dans la liste ordre_de_tour
        vitesse_perso = getattr(tourPerso, 'vit', 'N/A')
        #print(f"- {nom_perso} (Vitesse: {vitesse_perso})")

    return ordre_de_tour

def equipe_petit_vers_grand(a: list, b: list):
    liste_element = a + b
    perso_vivant = []
    perso_exeption = []

    for perso in liste_element:
        # 'perso' doit être un objet personnage avec un attribut 'vit' (vitesse)
        if hasattr(perso, 'vit'):
            perso_vivant.append([perso.vit, perso])
        else:  # Gérer les cas où un combattant n'a pas d'attribut 'vit' (par exemple, enregistrer ou sauter)
            perso_exeption.append(perso)

    liste_vitesse = []
    for info in perso_vivant: liste_vitesse.append(info[0])  # Extraire uniquement les vitesses pour le tri
    # Trier les vitesses du plus petit au plus grand en utilisant la fonction importée
    reajust_liste_vitesse = petit_vers_grand(liste_vitesse)
    # Reconstruire la liste des personnages dans l'ordre de reajust_liste_vitesse
    ordre_de_tour = []
    # Utiliser une copie de perso_vivant pour permettre la suppression des éléments, gérant correctement les vitesses identiques
    ajust_par_vitesse = [info for info in perso_vivant]  # Create a shallow copy

    for vitesse in reajust_liste_vitesse:
        for index, info in enumerate(ajust_par_vitesse):
            if info[0] == vitesse:
                ordre_de_tour.append(info[1])  # Add the character object
                ajust_par_vitesse.pop(index)  # Remove from copy to handle duplicates correctly
                break  # Found character for this vitesse, move to next vitesse
    ordre_de_tour += perso_exeption

    # Maintenant, 'ordre_de_tour' contient les objets personnages triés par vitesse (croissant).
    # Vous pouvez utiliser cette liste pour la séquence de combat.
    # Exemple : Afficher l'ordre des tours
    #print("\nOrdre des tours (par vitesse croissante):")
    for tourPerso in ordre_de_tour:
        nom_perso = getattr(tourPerso, 'nom', 'Personnage inconnu')  # On récupère l'attribut 'nom' des classes/sous_classe 'perso' dans la liste ordre_de_tour
        vitesse_perso = getattr(tourPerso, 'vit', 'N/A')
        #print(f"- {nom_perso} (Vitesse: {vitesse_perso})")

    return ordre_de_tour

if __name__ == "__main__":
    from random import randint
    test = []
    test.clear()
    for i in range(10):
        i = randint(1, 20)
        test.append(i)
    a = grand_vers_petit(test)
    b = petit_vers_grand(test)
    print(f"a : {a}")
    print(f"b : {b}")