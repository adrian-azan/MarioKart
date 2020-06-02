from kivy.app import App
from kivy.uix.widget import Widget

import tkinter as tk
from tile import *
from player import player
import json as js
import game as gm
import random as rn
import RandomCourseGenerator as randCourse
import re
def loadFile():
    def okClick():
        fileName = "savedGames\\" + fileNameEntry.get()
        if (not re.search("$.json",fileName)):
            fileName += ".json"

        with open(fileName, "r") as inputFile:
            gm.jsonTiles = js.load(inputFile)

        for jsonTile,boardTile in zip(gm.jsonTiles,gm.allTiles):
            boardTile.owner = jsonTile["owner"]
        gm.updateScores()
        popup.destroy()

    popup = tk.Tk()
    popup.title = "Save Game"
    fileNameLabel = tk.Label(popup, text= "Enter File Name")
    fileNameEntry = tk.Entry(popup)
    ok = tk.Button(popup,text="OK", command=okClick)

    
    fileNameLabel.pack()
    fileNameEntry.pack()
    ok.pack()
    popup.mainloop()


def saveFile():
    def okClick():
        fileName = "savedGames\\"+fileNameEntry.get()
        if (not re.search("$.json",fileName)):
            fileName += ".json"

        with open(fileName, "w") as outputFile:
            outputFile.write(js.dumps(gm.jsonTiles,indent=4))

        popup.destroy()

    for jsonTile,boardTile in zip(gm.jsonTiles,gm.allTiles):
        jsonTile["owner"] = boardTile.owner

    popup = tk.Tk()
    popup.title = "Save Game"
    fileNameLabel = tk.Label(popup, text= "Enter File Name")
    fileNameEntry = tk.Entry(popup)
    ok = tk.Button(popup,text="OK", command=okClick)

    
    fileNameLabel.pack()
    fileNameEntry.pack()
    ok.pack()
    popup.mainloop()

    
    




if __name__ == '__main__':
    window = tk.Tk()
    tileNames = []
    tileOwners = []
    
    
    menubar = tk.Menu(window)
    fileMenu = tk.Menu(menubar,tearoff=0)    
    editMenu = tk.Menu(menubar, tearoff=0)

    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_command(label="Load", command=loadFile)
    editMenu.add_command(label="Clear",command=gm.clearBoard)
    
    menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Edit", menu=editMenu)
    window.config(menu=menubar)
    
    
    with open("newMaster.json",'r') as jsonInput:
        gm.jsonTiles=js.load(jsonInput)
    
      
    i = 0
    j = 0
    for boardTile in gm.jsonTiles:        
            btn = tile(window, boardTile,(i,j))
            gm.allTiles.append(btn)
            btn.tile.grid(row=i,column=j,sticky="NSWE")
            window.rowconfigure(i,weight=1)
            window.columnconfigure(j,weight=1)

            j+=1
            if (j >= gm.COLS):
                j=0
                i+=1
            if i>= gm.ROWS:
                i=0
            
            
    
    window.rowconfigure(gm.ROWS,weight=1)

    gm.player1.setFrame(window,gm.ROWS)
    gm.player2.setFrame(window,gm.ROWS+1)

    generator = randCourse.RandomCourseGenerator(window)

    window.mainloop()
    