import asyncio
import websockets
import pandas as pd
from io import BytesIO
 
async def test():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send("hello")
        #response = await websocket.recv() # For non-binary data


        respBin = await websocket.recv()
        
        response = pd.read_json(BytesIO(respBin))
        print(response)


asyncio.get_event_loop().run_until_complete(test())