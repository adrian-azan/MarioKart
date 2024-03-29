from player import player


COLS = 14
ROWS = 6
player1 = player("Adrian","red")
player2 = player("Amanda","blue")
allTiles = []
jsonTiles = []
DEFAULT_COLOR = ('old lace','lavender')


def isCaptured(row,col):       
    captured = True
    if (row < 0 or row >=ROWS or col < 0 or col >= COLS):
        return False

    if (allTiles[row*COLS+col].tile['bg'] not in DEFAULT_COLOR):
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
        
    if (bottom != None and bottom['bg'] in DEFAULT_COLOR):
        captured = False
    if (top != None and top['bg'] in DEFAULT_COLOR):
        captured = False
    if (left != None and left['bg'] in DEFAULT_COLOR):
        captured = False
    if (right != None and right['bg'] in DEFAULT_COLOR):
        captured = False

    return captured

def checkCaptures(player,row,col):
    
    if isCaptured(row,col-1) == True: #left
        allTiles[row*COLS+(col-1)].tile.configure(bg=player.color)
        allTiles[row*COLS+(col-1)].tileLabel.configure(bg=player.color)
        allTiles[row*COLS+(col-1)].owner = player.name
    
    if isCaptured(row,col+1) == True: #right
        allTiles[row*COLS+(col+1)].tile.configure(bg=player.color)
        allTiles[row*COLS+(col+1)].tileLabel.configure(bg=player.color)
        allTiles[row*COLS+(col+1)].owner = player.name

    if isCaptured(row-1,col) == True: #top
        allTiles[(row-1)*COLS+(col)].tile.configure(bg=player.color)
        allTiles[(row-1)*COLS+(col)].tileLabel.configure(bg=player.color)
        allTiles[(row-1)*COLS+(col)].owner = player.name

    if isCaptured((row+1),col) == True: #bottom
        allTiles[(row+1)*COLS+(col)].tile.configure(bg=player.color)
        allTiles[(row+1)*COLS+(col)].tileLabel.configure(bg=player.color)
        allTiles[(row+1)*COLS+(col)].owner = player.name

def updateScores():
    player1.score = 0
    player2.score = 0
    for tile in allTiles:
        if tile.owner == player1.name:
            tile.tile["bg"] = player1.color
            tile.tileLabel["bg"] = player1.color
            player1.score += 1
        
        elif tile.owner == player2.name:
            tile.tile["bg"] = player2.color
            tile.tileLabel["bg"] = player2.color
            player2.score += 1

    player1.updateScore()
    player2.updateScore()

def clearBoard():
    for tile in allTiles:
        tile.clear()
        updateScores()