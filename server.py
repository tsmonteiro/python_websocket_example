import asyncio
import websockets
import pandas as pd
 

async def request_handler(websocket, path):
 
    data = await websocket.recv()
 
    df = pd.DataFrame({"Data":[1,2,3,4]})
    dfBytes = df.to_json().encode()
    # reply = f"Data recieved as:  {data}!"
    
    await websocket.send(dfBytes)
 
 
 
websocket_server = websockets.serve(request_handler, "localhost", 8000)
 

 
asyncio.get_event_loop().run_until_complete(websocket_server)
 
asyncio.get_event_loop().run_forever()