def produit_en_croix(a1=None, b1=None, a2=None, b2=None):
    num_val = [a1, b1, a2, b2]
    chercher = None
    retour_val = 0
    """
    Produit en croix chercher la valeur manquante
    #  a1     a2  |   05     10
    # ---- = ---- |  ---- = ----
    #  b1     b2  |   10     20
    # a1 = (b1 * a2) / b2
    # b1 = (a1 * b2) / a2
    # a2 = (a1 * b2) / b1
    # b2 = (b1 * a2) / a1
    """
    for i, valeur in enumerate(num_val):
        print(i, valeur)
        if valeur == None:
            retour_val += 1
    print(retour_val)
    if retour_val != 1:
        print("erreur")
        return "erreur"
    if a1 is None:
        chercher = (( b1 * a2 ) / b2)
        print(chercher)
        return chercher
    if b1 is None:
        chercher = (( a1 * b2 ) / a2)
        print(chercher)
        return chercher
    if a2 is None:
        chercher = (( a1 * b2 ) / b1)
        print(chercher)
        return chercher
    if b2 is None:
        chercher = (( b1 * a2 ) / a1)
        print(chercher)
        return chercher

produit_en_croix(a1=None, b1=0.1, a2=50, b2=1000)