import tkinter as tk


class player:

    def __init__(self,name, color):
        self.name = name
        self.color = color
        self.score = 0        
       

    def setFrame(self,window,row):
        self.scoreFrame = tk.Frame(master=window,bd=10,bg='old lace')
        self.scoreFrame.grid(row=row,column=0,columnspan=4,sticky="we")
        self.scoreLabel = tk.Label(self.scoreFrame, text=self.name + ": " + str(self.score), 
                                    font=18, fg=self.color,bd=10, bg='old lace')       
        
        self.scoreLabel.pack(anchor="nw")

    def updateScore(self):
        self.scoreLabel.configure(text=self.name + ": " + str(self.score))
