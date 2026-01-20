from RPG_Assembly.classe.magie.medical.sort_soutien import Sort_soin


class PremierSecours(Sort_soin):
    def __init__(self, nom="premier secours", cout_pm=3, soin=15):
        super().__init__(nom, cout_pm, soin)