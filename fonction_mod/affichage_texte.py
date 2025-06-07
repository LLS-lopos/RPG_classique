def affichage_texte(msg):
    # variable
    liste_taille = []
    taille_msg = None

    # estimé le taille maximum du texte
    if type(msg) == list:
        for i in msg:
            liste_taille.append(len(i))
        taille_msg = max(liste_taille)
    else:
        taille_msg = len(msg)

    # affichage du texte
    print("+-"+"-"*taille_msg+"-+")
    if type(msg) == list:
        for i in msg:
            ajust = taille_msg - len(i)
            print("| "+i+" "*ajust+" |")
    else:
        print("| "+msg+" |")
    print("+-"+"-"*taille_msg+"-+")

