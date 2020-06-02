from kivy.app import App
from kivy.uix.widget import Widget

import tkinter as tk
from tile import *
from player import player
import game as gm
import random as rn
import RandomCourseGenerator as randCourse
def loadFile():
    

    def okClick():
        fileName = fileNameEntry.get()
        if (fileName[-4:] != ".txt"):
            fileName += ".txt"

        input = open(fileName,'r')
        names = input.readlines()
        for name in names:
            name = name.split()
            tileNames.append(name[0])
            tileOwners.append(name[1])   

        input.close() 
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
        fileName = fileNameEntry.get()
        if (fileName[-4:] != ".txt"):
            fileName += ".txt"

        output = open(fileName,'w')
        for tile in gm.allTiles:
            name = tile.name
            owner = tile.owner
            output.write(name + " " + owner + "\n")
             

        output.close() 
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

    
    




if __name__ == '__main__':
    window = tk.Tk()
    tileNames = []
    tileOwners = []
    
    
    menubar = tk.Menu(window)
    fileMenu = tk.Menu(menubar,tearoff=0)
    
    editMenu = tk.Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Save", command=saveFile)
    editMenu.add_command(label="Clear",command=gm.clearBoard)
    
    menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Edit", menu=editMenu)
    window.config(menu=menubar)



    input = open("master.txt",'r')
    names = input.readlines()
    for name in names:
        name = name.split()
        tileNames.append(name[0])
        tileOwners.append(name[1])   

    input.close()     
    
    pretty = 0
   

    for i in range(gm.ROWS):
        for j in range(gm.COLS):
            
            btn = tile(window, tileNames[i*gm.COLS+j], tileOwners[i*gm.COLS+j],i,j)
            gm.allTiles.append(btn)
            btn.tile.grid(row=i,column=j,sticky="NSWE")
            window.rowconfigure(i,weight=1)
            window.columnconfigure(j,weight=1)
            
            
    
    window.rowconfigure(gm.ROWS,weight=1)

    gm.player1.setFrame(window,gm.ROWS)
    gm.player2.setFrame(window,gm.ROWS+1)

    generator = randCourse.RandomCourseGenerator(window)

    window.mainloop()
    