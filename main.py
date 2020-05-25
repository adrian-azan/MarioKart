from kivy.app import App
from kivy.uix.widget import Widget

import tkinter as tk
from button import *



if __name__ == '__main__':
    window = tk.Tk()
    tileNames = []
    tileOwners = []
    

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
            
            
    
   

    window.mainloop()
    