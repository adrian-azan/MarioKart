import tkinter as tk
from game import *



class button:
    def leftClick(self,event):
        if (self.tile['background'] == player1.color):
            self.tile.configure(bg = 'old lace')
            self.tileLabel.configure(bg = 'old lace')
        else:
            self.tile.configure(bg=player1.color)
            self.tileLabel.configure(bg=player1.color)

        if checkCapture(self.row,self.col-1) == True: #left
            allTiles[self.row*COLS+(self.col-1)].tile.configure(bg=player1.color)
            allTiles[self.row*COLS+(self.col-1)].tileLabel.configure(bg=player1.color)
        
        if checkCapture(self.row,self.col+1) == True: #right
            allTiles[self.row*COLS+(self.col+1)].tile.configure(bg=player1.color)
            allTiles[self.row*COLS+(self.col+1)].tileLabel.configure(bg=player1.color)
        
        if checkCapture(self.row-1,self.col) == True: #top
            allTiles[(self.row-1)*COLS+(self.col)].tile.configure(bg=player1.color)
            allTiles[(self.row-1)*COLS+(self.col)].tileLabel.configure(bg=player1.color)

        if checkCapture((self.row+1),self.col) == True: #bottom
            allTiles[(self.row+1)*COLS+(self.col)].tile.configure(bg=player1.color)
            allTiles[(self.row+1)*COLS+(self.col)].tileLabel.configure(bg=player1.color)
        

    def rightClick(self,event):
        #if tile is already color selected, will turn neutral
        if (self.tile['background'] == player2.color):
            self.tile.configure(bg = 'old lace')
            self.tileLabel.configure(bg = 'old lace')
        else:
            self.tile.configure(bg=player2.color)
            self.tileLabel.configure(bg=player2.color)
        
        if checkCapture(self.row,self.col-1) == True: #left
            allTiles[self.row*COLS+(self.col-1)].tile.configure(bg=player2.color)
            allTiles[self.row*COLS+(self.col-1)].tileLabel.configure(bg=player2.color)
        
        if checkCapture(self.row,self.col+1) == True: #right
            allTiles[self.row*COLS+(self.col+1)].tile.configure(bg=player2.color)
            allTiles[self.row*COLS+(self.col+1)].tileLabel.configure(bg=player2.color)
        
        if checkCapture(self.row-1,self.col) == True: #top
            allTiles[(self.row-1)*COLS+(self.col)].tile.configure(bg=player2.color)
            allTiles[(self.row-1)*COLS+(self.col)].tileLabel.configure(bg=player2.color)

        if checkCapture((self.row+1),self.col) == True: #bottom
            allTiles[(self.row+1)*COLS+(self.col)].tile.configure(bg=player2.color)
            allTiles[(self.row+1)*COLS+(self.col)].tileLabel.configure(bg=player2.color)

        
        

    def __init__(self,window, name, owner,row,col):
        self.owner = owner
        self.name = name
        self.row = row
        self.col = col

        #Every board space has a frame and a label
        self.tile = tk.Frame(window, bg='old lace', bd=10,highlightbackground="black", 
                            highlightcolor="black", highlightthickness=1)
        self.tileLabel = tk.Label(self.tile, bg = 'old lace', text=self.name + "\n"+ self.owner, anchor="center",bd=10)
        self.tileLabel.pack(expand=True,fill="both")

        #Bind tiles and labels to have left and right click functions
        self.tile.bind("<Button-1>", self.leftClick)
        self.tileLabel.bind("<Button-1>", self.leftClick)
        self.tile.bind("<Button-3>", self.rightClick)
        self.tileLabel.bind("<Button-3>", self.rightClick)

        