import asyncio
import websockets

async def echo(websocket, path):
    await websocket.send("¡Conexión establecida!")
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        await websocket.send(f"Respuesta: {message}")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
