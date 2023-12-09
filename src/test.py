import requests

SERVER_IP = "https://134.209.240.184:8081"
SERVER_IP_2 = "https://134.209.244.186:8081"


login_data = {
        "username":"UpalaZuba",
        "password":"4q78qSQJ0E"
    }

jwt = ""

def login():
    response = requests.post(SERVER_IP_2+"/user/login", json=login_data)

    if response.status_code == 200:
        data = response.json()
        print(data)
        jwt = data.get("token")
    else:
        print({"error":f"STATUS CODE {response.status_code}"})

# def 


