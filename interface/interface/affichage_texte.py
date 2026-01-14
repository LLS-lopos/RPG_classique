def affichage_texte(msg: (str, int, bool, tuple, dict, list), titre: str = None, fin: str = None):
    # variable
    liste_taille = []
    taille_msg = 0
    bloc = ""

    # estimé le taille maximum du texte
    if type(msg) == list:
        taille_msg = taille_liste(msg)
        liste_taille.append(taille_msg)
    elif type(msg) == tuple:
        taille_msg = taille_tuple(msg)
        liste_taille.append(taille_msg)
    elif type(msg) == dict:
        for cle, valeur in enumerate(msg):
            liste_taille.append(len(str(valeur)))
            if type(msg[valeur]) == tuple:
                taille_msg = taille_tuple(msg[valeur])
                liste_taille.append(taille_msg)
            elif type(msg[valeur]) == list:
                taille_msg = taille_liste(msg[valeur])
                liste_taille.append(taille_msg)
            elif type(msg[valeur]) == dict:
                taille_msg = taille_dictionnaire(msg[valeur])
                liste_taille.append(taille_msg)
            else:
                liste_taille.append(len(str(f"    {msg[valeur]}")))
    else:
        liste_taille.append(len(str(msg)))
    if titre:
        liste_taille.append(len(str(titre)))
    if fin:
        liste_taille.append(len(str(fin)))

    # print(f"Liste Taille MSG - {liste_taille} -> maximum : {max(liste_taille)}")
    # affichage du texte
    # affiché le titre si existant
    if titre:
        bloc += affiche_titre(titre, max(liste_taille))
    if msg:
        # bloc += f"TYPE: {type(msg)}\n"
        if type(msg) == list:
            bloc += affiche_liste(msg, max(liste_taille))
        elif type(msg) == tuple:
            bloc += affiche_tuple(msg, max(liste_taille))
        elif type(msg) == dict:
            bloc += affiche_dictionnaire(msg, max(liste_taille))
        else:
            bloc += affichage_simple(msg, max(liste_taille))
    if fin:
        bloc += fermer_affiche(fin, max(liste_taille))
    else:
        bloc += f"+-{"-" * max(liste_taille)}-+\n"

    return print(bloc)


def taille_tuple(tupple) -> int | None:
    taille = []
    for i in tupple:
        taille.append(len(str(i)))
    if taille:
        return max(taille)


def taille_liste(liste) -> int | None:
    taille = []
    for i in liste:
        taille.append(len(str(i)))
    if taille:
        return max(taille)


def taille_dictionnaire(dicto) -> int | None:
    taille = []
    for cle, valeur in enumerate(dicto):
        taille.append(len(str(valeur)))
        if type(dicto[valeur]) == list:
            recup = taille_liste(dicto[valeur])
            taille.append(recup + 4)
        elif type(dicto[valeur]) == tuple:
            recup = taille_tuple(dicto[valeur])
            taille.append(recup + 4)
        elif type(dicto[valeur]) == dict:
            taille_dictionnaire(dicto[valeur])
        else:
            taille.append(len(str(dicto[valeur])) + 4)

    if taille:
        return max(taille)


def affichage_simple(af_text: str, taille_max, decalage=1) -> str | None:
    texte = ""
    reduction = 0
    if decalage > 1:
        reduction = -decalage
    if len(str(af_text)) < taille_max:
        reste = taille_max - len(str(af_text)) + reduction
        texte = f"|{" " * decalage}{af_text}{" " * reste} |\n"
    else:
        texte = f"|{" " * decalage}{af_text}{" " * decalage}|\n"
    return texte


def affiche_titre(af_titre, taille_max) -> str | None:
    texte = ""
    if len(str(af_titre)) < taille_max:
        reste = taille_max - len(str(af_titre))
        moitier = reste // 2
        difference = reste % 2
        texte = f"+-{"-" * moitier}{af_titre}{"-" * moitier}{"-" * difference}-+\n"
    else:
        texte = f"+-{af_titre}-+\n"
    return texte


def affiche_tuple(af_tuple, taille_max, decalage=1) -> str | None:
    texte = ""
    for i in af_tuple:
        texte += affichage_simple(i, taille_max, decalage)
    return texte


def affiche_liste(af_liste, taille_max, decalage=1) -> str | None:
    texte = ""
    for i in af_liste:
        texte += affichage_simple(i, taille_max, decalage)
    return texte


def affiche_dictionnaire(ad_dict, taille_max, decalage=1) -> str | None:
    texte = ""
    for index, cle in enumerate(ad_dict):
        texte += affichage_simple(cle, taille_max)
        if type(ad_dict[cle]) == list:
            texte += affiche_liste(ad_dict[cle], taille_max, 2)
        elif type(ad_dict[cle]) == tuple:
            texte += affiche_tuple(ad_dict[cle], taille_max, 2)
        elif type(ad_dict[cle]) == dict:
            for i in ad_dict[cle]:
                texte += affichage_simple(i, taille_max, 2)
                if type(ad_dict[cle][i]) == list:
                    texte += affichage_simple("--", taille_max, 4)
                    texte += affiche_liste(ad_dict[cle][i], taille_max, 4)
                elif type(ad_dict[cle][i]) == tuple:
                    texte += affichage_simple("--", taille_max, 4)
                    texte += affiche_tuple(ad_dict[cle][i], taille_max, 4)
                elif type(ad_dict[cle][i]) == dict:
                    texte += affichage_simple("--", taille_max, 4)
                    for n_cle, externe in enumerate(ad_dict[cle][i]):
                        texte += affichage_simple(externe, taille_max, 4)
                        texte += affichage_simple(ad_dict[cle][i][externe], taille_max, 6)
                else:
                    texte += affichage_simple("--", taille_max, 4)
                    texte += affichage_simple(ad_dict[cle][i], taille_max, 4)
        else:
            texte += affichage_simple(ad_dict[cle], taille_max, 2)
    return texte


def fermer_affiche(del_af, taille_max) -> str | None:
    texte = ""
    if len(str(del_af)) < taille_max:
        reste = taille_max - len(str(del_af))
        moitier = reste // 2
        difference = reste % 2
        texte = f"+-{"-" * moitier}{del_af}{"-" * moitier}{"-" * difference}-+\n"
    else:
        texte = f"+-{del_af}-+\n"
    return texte


if __name__ == "__main__":
    dico = {
        "nom": "Jack",
        "polo": [
            "1 kaka",
            "2 pull",
            "3 Poullue"],
        "jack": True,
        "heure": 5.0,
        "est": 10,
        "tutuple": (20.01, 2, 0.3),
        "note": {
            "n_nom": "slime",
            "attaque": 5,
            "defense": 2,
            "exp": 22.01,
            "mort": False,
            "codi": (2.0, "trt"),
            "topo": {
                0: "sfqd",
                1: "qfdsf"
            },
            "gg_course": ["beurre", "sucre", "lait", 20, (56, "att", 20)]
        }
    }
    listo = ["pol", "li", "ice"]
    texte = "pazkkf efzef"
    tutuple = (20.01, 2, 3.3)
    affichage_texte(tutuple, "Test Tuple", "final")
    affichage_texte(texte, "Test Texte", "OM")
    affichage_texte(listo, "Test Liste", "PSG")
    affichage_texte(dico, "Test Dictionnaire", "V0.1")
    affichage_texte("RPG GAME", "RPG ADVENTURE CLASSIQUE CLI", "v0.1")
