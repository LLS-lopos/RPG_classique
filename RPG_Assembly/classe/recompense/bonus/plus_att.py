from RPG_Assembly.classe.recompense.bonus import Bonus


class bonusATT(Bonus):
    def __init__(self):
        super().__init__()
        # Un bonus sait :
        # comment il s’appelle
        # ce qu’il fait
        # comment s’appliquer au joueur