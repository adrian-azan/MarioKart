
from player import player

COLS = 14
ROWS = 6
player1 = player("Adrian","red")
player2 = player("Amanda","blue")
allTiles = []
DEFAULT_COLOR = 'old lace'


def isCaptured(row,col):
    p1Score = 0
    p2Score = 0
    
    captured = True
    if (row < 0 or row >=ROWS or col < 0 or col >= COLS):
        return False

    if (allTiles[row*COLS+col].tile['bg'] != DEFAULT_COLOR):
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

def checkCaptures(player,row,col):
    
    if isCaptured(row,col-1) == True: #left
        allTiles[row*COLS+(col-1)].tile.configure(bg=player.color)
        allTiles[row*COLS+(col-1)].tileLabel.configure(bg=player.color)
    
    if isCaptured(row,col+1) == True: #right
        allTiles[row*COLS+(col+1)].tile.configure(bg=player.color)
        allTiles[row*COLS+(col+1)].tileLabel.configure(bg=player.color)
    
    if isCaptured(row-1,col) == True: #top
        allTiles[(row-1)*COLS+(col)].tile.configure(bg=player.color)
        allTiles[(row-1)*COLS+(col)].tileLabel.configure(bg=player.color)

    if isCaptured((row+1),col) == True: #bottom
        allTiles[(row+1)*COLS+(col)].tile.configure(bg=player.color)
        allTiles[(row+1)*COLS+(col)].tileLabel.configure(bg=player.color)

def updateScores():
    player1.score = 0
    player2.score = 0
    for tile in allTiles:
        if tile.tile['bg'] == player1.color:
            player1.score += 1
        
        elif tile.tile['bg'] == player2.color:
            player2.score += 1

    player1.updateScore()
    player2.updateScore()
