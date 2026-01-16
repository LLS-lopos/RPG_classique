class vegetation:
    def __init__(self, nom, init_temps, vit_pousse, mure=False, cueillir=False):
        super().__init__()
        self._nom = nom
        self._init_temps = init_temps
        self._vit_pousse = vit_pousse
        self._mure = mure
        self._cueillir = cueillir

    def check_mure(self):
        if not self._mure:
            self._init_temps += 1
            if self._init_temps == self._vit_pousse:
                self._mure = True

    def recolter(self):
        if self._mure:
            self._init_temps = 0
            self._mure = False

    def __str__(self):
        etat = ''
        if self._mure:
            etat = " [mure]"
        return f"{self._nom} ({self._init_temps}/{self._vit_pousse}){etat}"

    def __repr__(self):
        etat = ''
        if self._mure:
            etat = " [mure]"
        return f"{self._nom} ({self._init_temps}/{self._vit_pousse}){etat}"