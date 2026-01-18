try:
    import tkinter
    from tkinter.scrolledtext import ScrolledText
except:
    pass

class GameUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Rogue-like")

        # Layout principal
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Zone pour montrer les stats
        stats_frame = tkinter.Frame(self.root)
        stats_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.player_stats = tkinter.Label(
            stats_frame, text="JOUEUR", anchor="w", justify="left",
            width=40, padx=10, pady=10, relief="groove"
        )
        self.player_stats.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.enemy_stats = tkinter.Label(
            stats_frame, text="ENNEMI", anchor="w", justify="left",
            width=40, padx=10, pady=10, relief="groove"
        )
        self.enemy_stats.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Console
        self.console = ScrolledText(
            self.root, height=15, state="disabled", wrap=tkinter.WORD
        )
        self.console.pack(fill=tkinter.BOTH, padx=10, pady=10, expand=True)

        # Zone d'entrée de texte
        input_frame = tkinter.Frame(self.root)
        input_frame.pack(fill=tkinter.X, padx=10, pady=5)

        self.input_var = tkinter.StringVar()
        self.input_entry = tkinter.Entry(input_frame, textvariable=self.input_var)
        self.input_entry.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

        self.submit_button = tkinter.Button(
            input_frame, text="OK", command=self._submit_input
        )
        self.submit_button.pack(side=tkinter.RIGHT)

        self._waiting_input = False
        self._last_input = None

        self.input_entry.bind("<Return>", lambda e: self._submit_input())

    # ===============================
    # API UTILISABLE PAR LE JEU
    # ===============================

    def print(self, text):
        """Affiche du texte dans la console."""
        self.console.config(state="normal")
        self.console.insert(tkinter.END, str(text) + "\n")
        self.console.see(tkinter.END)
        self.console.config(state="disabled")
        self.root.update()

    def set_player_stats(self, text):
        """Met à jour la zone de stats du joueur."""
        self.player_stats.config(text=text)
        self.root.update()

    def set_enemy_stats(self, text):
        """Met à jour la zone de stats de l'ennemi."""
        self.enemy_stats.config(text=text)
        self.root.update()

    def input(self, prompt="> "):
        """
        Équivalent graphique de input().
        Bloque jusqu'à ce que l'utilisateur valide.
        """
        self.print(prompt)
        self._waiting_input = True
        self._last_input = None
        self.input_entry.focus()

        while self._waiting_input:
            self.root.update()

        return self._last_input

    def mainloop(self):
        self.root.mainloop()

    # ===============================
    # MÉTHODES INTERNES
    # ===============================

    def _submit_input(self):
        if not self._waiting_input:
            return

        self._last_input = self.input_var.get()
        self.input_var.set("")
        self._waiting_input = False