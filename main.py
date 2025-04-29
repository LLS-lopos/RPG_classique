from classes.monstre.p_splip import Splip
from classes.perso import personnage
from fonction_mod.FM_groupe_ennemi import groups_ennemi
from fonction_mod.M_combat_simple import combat_simple
from fonction_mod.M_combat_un_contre_group import combat_un_contre_group

HERO = personnage("Polo", 1000, 3)
ins_splip = Splip()

group1 = groups_ennemi(20)


def main():
    main_menu = input(f"0-combat simple\n1-groupe\n")
    if main_menu == "0":
        combat_simple(HERO, ins_splip)
    elif main_menu == "1":
        combat_un_contre_group(HERO, group1)
    print("fin")


if __name__ == '__main__':
    main()
