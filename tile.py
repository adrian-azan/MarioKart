import tkinter as tk
import game as gm



class tile:
    def leftClick(self,event):
        if (self.tile['background'] == gm.player1.color):
            self.tile.configure(bg = 'old lace')
            self.tileLabel.configure(bg = 'old lace')
        else:
            self.tile.configure(bg=gm.player1.color)
            self.tileLabel.configure(bg=gm.player1.color)
        
        gm.checkCaptures(gm.player1,self.row,self.col)
        gm.updateScores()

    def rightClick(self,event):
        #if tile is already color selected, will turn neutral
        if (self.tile['background'] == gm.player2.color):
            self.tile.configure(bg = 'old lace')
            self.tileLabel.configure(bg = 'old lace')
        else:
            self.tile.configure(bg=gm.player2.color)
            self.tileLabel.configure(bg=gm.player2.color)
        
        gm.checkCaptures(gm.player2,self.row,self.col)
        gm.updateScores()

        
        

    def __init__(self,window, name, owner,row,col):
        self.owner = owner
        self.name = name
        self.row = row
        self.col = col

        #Every board space has a frame and a label
        
        
        if(self.name[:3] == "SPA"):
            self.tile = tk.Frame(window, bg='lavender', bd=10,highlightbackground="black", 
                            highlightcolor="black", highlightthickness=1)
            self.tileLabel = tk.Label(self.tile, bg = 'lavender', text=self.name +"\n", anchor="w",bd=10)
        else:
            self.tile = tk.Frame(window, bg='old lace', bd=10,highlightbackground="black", 
                            highlightcolor="black", highlightthickness=1)
            self.tileLabel = tk.Label(self.tile, bg = 'old lace', text=self.name +"\n", anchor="w",bd=10)

        self.tileLabel.pack(expand=True,fill="both")
        #Bind tiles and labels to have left and right click functions
        self.tile.bind("<Button-1>", self.leftClick)
        self.tileLabel.bind("<Button-1>", self.leftClick)
        self.tile.bind("<Button-3>", self.rightClick)
        self.tileLabel.bind("<Button-3>", self.rightClick)

    def clear(self):
        self.owner = ""
        if(self.name[:3] == "SPA"):
            self.tileLabel['bg'] = gm.DEFAULT_COLOR[1]
            self.tile['bg'] = gm.DEFAULT_COLOR[1]
        
        else:
            self.tileLabel['bg'] = gm.DEFAULT_COLOR[0]
            self.tile['bg'] = gm.DEFAULT_COLOR[0]