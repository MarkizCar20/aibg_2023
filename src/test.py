import requests
import asyncio
import aiohttp

SERVER_IP = "http://134.209.240.184:8081"
SERVER_IP_2 = "http://134.209.244.186:8081"

username = "UpalaZuba"
jwt = ""
game_id = ""
headers = {
    "Content-type":"application/json",
    "Authorization":f"Bearer {jwt}" 
}

def login(user):
    login_data = {
        "username":f"{user}",
        "password":"4q78qSQJ0E"
    }
    response = requests.post(SERVER_IP_2 + "/user/login", json=login_data)
    if response.status_code == 202:
        data = response.json()
        jwt = data.get("token")
    else:
        print({"error":f"STATUS CODE {response.status_code}"})
    return jwt

def createGame(team2, team3, team4):
    create_game = {
        "playerUsernames":["UpalaZuba1", "UpalaZuba2", "UpalaZuba3", "UpalaZuba4"],
        "mapName": "test1.txt"
    }
    response = requests.post(SERVER_IP_2 + "/game/createGame", json=create_game, headers=headers)
    data = response.json()
    if response.status_code == 201:
        game_id = data.get("gameId")
    else:
        print({"error":f"STATUS CODE {response.status_code}"})
    print(data.get("message"))

async def joinGame(session, token):
    headers = {
        "Content-type":"application/json",
        "Authorization":f"Bearer {token}" 
    }
    async with session.get(SERVER_IP_2+'/game/joinGame', headers=headers) as response:
        return await response.json()
    

