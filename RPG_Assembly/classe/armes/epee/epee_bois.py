from RPG_Assembly.classe.armes.arme import Arme


class epee_bois(Arme):
    def __init__(self, nom="épée de bois", att=3):
        super().__init__(nom, att)