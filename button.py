import tkinter as tk

class button:
    def __init__(self,window, name, owner):
        self.owner = owner
        self.name = name
        self.tile = tk.Frame(window, bd=10,highlightbackground="black", 
                            highlightcolor="black", highlightthickness=1)
        self.tileLabel = tk.Label(self.tile, text=self.name + "\n"+ self.owner, anchor="center",bd=10)
        self.tileLabel.pack(expand=True,fill="both")

        