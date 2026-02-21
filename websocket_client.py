import asyncio
import websockets
from websockets import ServerConnection

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hey server"
        print(f"Sending message: {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Received message: {response}")

asyncio.run(client())