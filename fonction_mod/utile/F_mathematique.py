def arrondir_entier_superieur(valeur: float):
    val = str(valeur).split(".")
    if not valeur:
        return
    if len(val) == 1:
        sortie = int(val[0])
        print(sortie)
        return sortie
    else:
        entier = int(val[0])
        list_decimal = []
        for i in val[-1]:
            list_decimal.append(i)
        while list_decimal:
            if len(list_decimal) > 3:
                list_decimal.pop(-1)
            else: break
        decimal = int("".join(list_decimal))

        if len(val[-1]) == 1 and decimal >= 5:
            entier += 1
            return entier
        elif len(val[-1]) == 2 and decimal >= 50:
            entier += 1
            return entier
        elif len(val[-1]) == 3 and decimal >= 500:
            entier += 1
            return entier
        else:
            return entier

if __name__ == "__main__":
    arrondir_entier_superieur(5.6)