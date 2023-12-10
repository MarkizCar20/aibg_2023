from game_state import state_example

myID = 0
state = state_example

def getMyID():
    return state["playerIdx"]

def findPlayerByID(id):
    if state["gameState"][f"player{id}"] != {}:
        return state["gameState"]["player1"]
    else:
        return -1    

def getHealth(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["health"]

def getMyHealth():
    return state["gameState"][f"player{myID}"]["health"]

def getAttackPow(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["attackPower"]   

def getMyAttackPow():
    return state["gameState"][f"player{myID}"]["attackPower"]

def getQ(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["q"]   

def getR(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["r"] 

def getMyQ():
    return state["gameState"][f"player{myID}"]["q"]

def getMyR():
    return state["gameState"][f"player{myID}"]["r"]

def getScore(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["score"]

def getMyScore():
    return state["gameState"][f"player{myID}"]["score"]

def getSkull(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["skull"]
    
def getMySkull():
    return state["gameState"][f"player{myID}"]["skull"]
    
def getScoreLvl(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["scoreLevel"]

def getMyScoreLvl():
    return state["gameState"][f"player{myID}"]["scoreLevel"]

def getSword(id):
    player_available = findPlayerByID(id)
    if player_available == -1:
        return -1
    else:
        return state["gameState"][f"player{id}"]["sword"]

def getMySword():
    return state["gameState"][f"player{myID}"]["sword"]

def getDistance(id1, id2):
    player_available1 = findPlayerByID(id1)
    player_available2 = findPlayerByID(id2)

    if player_available1 != -1 and player_available2 != -1:
        return int((abs(getQ(id1)-getQ(id2))+abs(getR(id1)-getR(id2)))/2)
    else:
        return -1
    
def getTile(q, r):
    try:
        tiles = state["gameState"]["map"]["tiles"]

        # Iterate through the tiles to find the one with matching q and r
        for row in tiles:
            for tile in row:
                if tile["q"] == q and tile["r"] == r:
                    return tile

        # If coordinates not found, raise an exception
        raise ValueError("Coordinates not found in the map.")

    except KeyError:
        raise ValueError("Invalid game state structure.")

#treba dohvatiti najblize lisce ili drvo

# testiranje

print(getMyID())
myID = getMyID()
print(findPlayerByID(1))
print(getHealth(4))
print(getMyHealth())

print(getAttackPow(4))
print(getMyAttackPow())

print(getQ(2))
print(getMyR())

print(getDistance(1, 4))
print(getDistance(1, 3))

print(getTile(1, -13))