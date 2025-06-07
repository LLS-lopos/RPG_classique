def affichage_texte(msg, titre = None):
    # variable
    liste_taille = []
    taille_msg = None

    # estimé le taille maximum du texte
    if type(msg) == list:
        for i in msg:
            liste_taille.append(len(str(i)))
        taille_msg = max(liste_taille)
    else:
        taille_msg = len(msg)

    # affichage du texte
    if titre is not None:
        if len(titre) > taille_msg:
            taille_msg = len(titre)
        else:
            taille_titre: int = taille_msg-len(titre)
            print("+-"+"-"*(taille_titre//2)+titre+"-"*(taille_titre//2)+"-"*(taille_titre%2)+"-+")
    else:
        print("+-"+("-"*taille_msg)+"-+")
    if type(msg) == list:
        for i in msg:
            ajust = taille_msg - len(str(i))
            print("| "+str(i)+" "*ajust+" |")
    else:
        print("| "+msg+" |")
    print("+-"+"-"*taille_msg+"-+")

