from kivy.app import App
from kivy.uix.widget import Widget

import tkinter as tk
from button import *
from player import player

def saveFile():
    def okClick():
        fileName = fileNameEntry.get()
        print(fileName)
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
    editMenu.add_command(label="Clear",command=clearBoard)
    
    menubar.add_cascade(label="File", menu=fileMenu)
    menubar.add_cascade(label="Edit", menu=editMenu)
    window.config(menu=menubar)



    input = open("master.txt",'r')
    names = input.readlines()
    for name in names:
        name = name.split()
        tileNames.append(name[0])
        tileOwners.append(name[1])        
    
    
    for i in range(ROWS):
        for j in range(COLS):
            
            btn = button(window, tileNames[i*COLS+j], tileOwners[i*COLS+j],i,j)
            allTiles.append(btn)
            btn.tile.grid(row=i,column=j,sticky="NSWE")
            window.rowconfigure(i,weight=1)
            window.columnconfigure(j,weight=1)
            
            
    
    window.rowconfigure(ROWS,weight=1)
    player1.setFrame(window,ROWS)
    player2.setFrame(window,ROWS+1)

    window.mainloop()
    