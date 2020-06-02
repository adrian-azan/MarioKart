from game import ROWS 
import random as rn
import tkinter as tk
class RandomCourseGenerator:

    def __init__(self,window):
        self.courses =  [[1,"Mushroom Cup","Mario Kart Stadium","Water Park","Sweet Sweet Canyon","Thwomp Ruins",],
            [1,"Flower Cup","Mario Circuit","Toad Harbour","Twisted Mansion","Shy Guy Falls"],
            [1,"Star Cup","Sunshine Airport","Dolphin Shoals","Electrodome","Mount Wario"],
            [1,"Special Cup","Cloudtop Cruise","Bone Dry Dunes","Bowser's Castle","Rainbow Road"],
            [1,"Shell Cup","Moo Moo Meadows (Wii)","Mario Circuit (GBA)","Cheep Cheep Beach (DS)","Toad's Turnpike (N64)"],
            [1,"Banana Cup", "Dry Dry Desert" ,"Donut Plains 3 (SNES)","Royal Raceway (N64)","DK Jungle (3DS)"],
            [1,"Leaf Cup","Wario Stadium","Sherbet Land (GCN)","Music Park (3DS)","Yoshi Valley (N64)"],
            [1,"Lightning Cup","Tick-Tock Clock (DS)","Piranha Plant Slide (3DS)","Grumble Volcano (Wii)","Rainbow Road (N64)"]]

        self.label = tk.Label(master=window,text="", font=14)
        self.button = tk.Button(master=window,text="Generate Course",
                                command=self.getCourse)
        self.button.grid(row=ROWS,column=5,columnspan=2)
        self.label.grid(row=ROWS,column=6, columnspan=6)

        
    


    def getCourse(self):
        cup = rn.randrange(0,len(self.courses))
        course = rn.randrange(2,len(self.courses[0]))
        self.label.configure(text=
            str(self.courses[cup][1]) + ": " + self.courses[cup][course])