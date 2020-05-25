
from player import *

player1 = player("Adrian","red")
player2 = player("Amanda","blue")
allTiles = []
DEFAULT_COLOR = 'old lace'
COLS = 14
ROWS = 6

def checkCapture(row,col):
    p1Score = 0
    p2Score = 0
    
    captured = True
    if (row < 0 or row >=ROWS or col < 0 or col >= COLS):
        return False

    if (col != 0):
        left = allTiles[row*COLS+(col-1)].tile
    else:
        left = None
    
    if (col != COLS-1):
        right = allTiles[row*COLS+(col+1)].tile
    else:
        right = None
    
    if (row != 0):
        top = allTiles[(row-1)*COLS+col].tile
    else:
        top = None

    if (row != ROWS-1):
        bottom = allTiles[(row+1)*COLS+col].tile
    else:
        bottom = None
        
    if (bottom != None and bottom['bg'] == DEFAULT_COLOR):
        captured = False
    if (top != None and top['bg'] == DEFAULT_COLOR):
        captured = False
    if (left != None and left['bg'] == DEFAULT_COLOR):
        captured = False
    if (right != None and right['bg'] == DEFAULT_COLOR):
        captured = False

    return captured
