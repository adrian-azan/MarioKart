import tkinter as tk
import game as gm



class tile:
    def leftClick(self,event):
        if (self.owner == gm.player1.name):
            self.tile.configure(bg = 'old lace')
            self.tileLabel.configure(bg = 'old lace')
            self.owner = "OPEN!"
        else:
            self.tile.configure(bg=gm.player1.color)
            self.tileLabel.configure(bg=gm.player1.color)
            self.owner = gm.player1.name
        
        gm.checkCaptures(gm.player1,self.row,self.col)
        gm.updateScores()

    def rightClick(self,event):
        #if tile is already color selected, will turn neutral
        if (self.owner == gm.player2.name):
            self.tile.configure(bg = 'old lace')
            self.tileLabel.configure(bg = 'old lace')
            self.owner = "OPEN!"
        else:
            self.tile.configure(bg=gm.player2.color)
            self.tileLabel.configure(bg=gm.player2.color)
            self.owner = gm.player2.name
        
        gm.checkCaptures(gm.player2,self.row,self.col)
        gm.updateScores()

        
        

    def __init__(self,window, boardTile,dim):
        self.owner = boardTile["owner"]
        self.name = boardTile["name"]
        self.row = dim[0]
        self.col = dim[1]

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