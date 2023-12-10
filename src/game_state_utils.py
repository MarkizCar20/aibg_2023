from game_state import state

myID = 0

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

def getDistance(id1, id2):
    player_available1 = findPlayerByID(id1)
    player_available2 = findPlayerByID(id2)

    if player_available1 != -1 and player_available2 != -1:
        return int((abs(getQ(id1)-getQ(id2))+abs(getR(id1)-getR(id2)))/2)
    else:
        return -1

#treba dohvatiti q i r od kovcega
#treba dohvatiti ostatak stvari kod player-a
#treba dohvatiti polje sa odredjenim koordinatama
#treba dohvatiti najblize lisce ili drvo

# if q and r in state["gameState"]["map"]["tiles"]

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