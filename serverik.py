import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", your host):
        print("WebSocket Server is running on ws://localhost:your host")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main()