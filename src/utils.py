from game_state_utils import state

import requests
import json

def calculate_new_position(position: dict, offset: dict, player: dict) -> None:
    position["q"] = player["q"] + offset["q"]
    position["r"] = player["r"] + offset["r"]


def compare_positions(first: dict, second: dict) -> bool:
    if first == {} or second == {}:
        return False
    
    if first["q"] == second["q"] and \
       first["r"] == second["r"]:
       return True
    
    return False


def set_avatars(avatars: dict, state: dict) -> None:
    avatars["player1"] = state["player1"]
    avatars["player2"] = state["player2"]
    avatars["player3"] = state["player3"]
    avatars["player4"] = state["player4"]


def can_hit(by: dict, who: dict) -> bool:
    if who == {}:
        return False

    by_i = 14 + by["r"]
    by_j = 14 - by["q"]

    who_i = 14 + who["r"]
    who_j = 14 - who["1"]

    return abs(by_i - who_i) == 1 and abs(by_j - who_j) == 1

#####################################################################

SERVER_ID = "134.209.240.184:8081"
MY_ID = 1
GAME_ID = 12

# state = {}

_params = {
    "playerId": MY_ID,
    "gameId": GAME_ID
}

player1 = {}
player2 = {}
player3 = {}
player4 = {}

_avatars = {
    "player1": player1,
    "player2": player2,
    "player3": player3,
    "player4": player4
}

_moves = ["nw", "w", "sw", "se", "e", "ne"] #ovo treba izmeniti
_offset = {
    "nw": {
        "q": 0,
        "r": -1,
        "s": 1
    },
    "w": {
        "q": -1,
        "r": 0,
        "s": 1
    },
    "sw": {
        "q": -1,
        "r": 1,
        "s": 0
    },
    "se": {
        "q": 0,
        "r": 1,
        "s": -1
    },
    "e": {
        "q": 1,
        "r": 0,
        "s": -1
    },
    "ne": {
        "q": 1,
        "r": -1,
        "s": 0
    }
}

_action = SERVER_ID + "/doAction"

def update_characters():
    player1 = state["player1"]
    player2 = state["player2"]
    player3 = state["player3"]
    player4 = state["player4"]


def move(direction: str) -> bool:
    # Check if invalid direction
    if direction not in _moves:
        return False

    global state
    map = state["map"]["tiles"]

    # Check if out of map
    position = {}
    calculate_new_position(position, _offset[direction], state["player1"])
    set_avatars(_avatars, state)

    if 15 in position.values() or -15 in position.values():
        print("IZLETEO IZ MAPE")
        return False

    i = 14 + position["q"] #ne znam da li ovo valja
    j = 14 - position["r"] #ne znam da li ovo valja
    
    # Check if can't move to tile
    if map[i][j]["tileType"] == "FULL":
        print("KRENUO NA FULL POLJE")
        return False
    
    # Check if entity on tile
    for avatar in _avatars.values():
        if compare_positions(position, avatar):
            print("KRENUO NA AVATARA")
            return False

    params = _params.copy()
    params["action"] = direction

    print(_action)
    print(params)

    req = requests.get(_action, params=params)

    if req.status != 200:
        print("UH OH")
        return False

    state = json.loads(req.text)

    return True


def hit(x: int) -> bool:
    if x not in range(1, 5):
        print("LOL")
        return False

    global state

    if not can_hit(state[f"player{MY_ID}"], state[f"player{x}"]):
        print("OUT OF RANGE")
        return False

    params = _params.copy()
    params["action"] = f"atk-{x}"

    return True


def get_legal_moves():
    pass