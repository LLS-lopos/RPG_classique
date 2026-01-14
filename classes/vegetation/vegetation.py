class vegetation:
    def __init__(self, nom, init_temps, vit_pousse, mure=False):
        super().__init__()
        self._nom = nom
        self._init_temps = init_temps
        self._vit_pousse = vit_pousse
        self._mure = mure

    def check_mure(self):
        if self._init_temps != self._vit_pousse:
            self._init_temps += 1
        else:
            self._mure = True



    def __str__(self):
        return f"classe -> {self._nom}"

    def __repr__(self):
        return f"classe -> {self._nom}"