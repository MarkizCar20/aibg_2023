from test import login, createGame, joinGame
import asyncio
import aiohttp

USERS = ["UpalaZuba1", "UpalaZuba2", "UpalaZuba3", "UpalaZuba4"]
tokens = []

for user in USERS:
    tokens.append(login(user))

createGame("UpalaZuba2", "UpalaZuba3", "UpalaZuba4")

async def joinGameMain():

    async with aiohttp.ClientSession() as session:
        tasks = []
        for token in tokens:
            tasks.append(joinGame(session, token))
        responses = await asyncio.gather(*tasks)

    for index, response in enumerate(responses, 1):
        print(f"Response {index}: {response}")

asyncio.run(joinGameMain())

