from random import randint

def combat_simple(hero, ennemi):
    perso = (hero, ennemi)
    while True:
        for i in perso:
            if i.ko is True:
                return
        print(f"{ennemi.nom} - PV: {"💚" * ennemi.pv}, ⚔️: {ennemi.att}")
        choix = input("1_att, 2_defence\n->")
        if choix == "1":
            hero.attaque(ennemi)
        elif choix == "2":
            print(f"{hero.nom} ne fait rien")
        else:
            print("1 ou 2 comme choix possible")

        if not ennemi.ko:
            choix_ennemi = randint(0, 5)
            if choix_ennemi < 4:
                ennemi.attaque(hero)
            if choix_ennemi >= 4:
                print(f"{ennemi.nom} ne fait rien")