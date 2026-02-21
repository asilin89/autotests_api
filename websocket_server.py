import asyncio
import websockets
from websockets import ServerConnection

async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Received message: {message}")
        response = f"Server received message: {message}"
        await websocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print(f"WebSocket server is running on ws://localhost:{8765}")
    await server.wait_closed()

asyncio.run(main())

