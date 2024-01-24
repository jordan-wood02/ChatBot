import os
from fastapi import APIRouter, FastAPI, WebSocket, Request, BackgroundTasks, HTTPException
import uuid
from ..socket.connection import ConnectionManager

chat = APIRouter()
manager = ConnectionManager()

# @route    POST /token
# @desc     Route to generate chat token
# @access   Public


@chat.post("/token")
async def token_generator(name: str, request: Request):

    # Name is required
    if name == "":
        raise HTTPException(status_code=400, detail={
            "loc": "name", "msg": "Enter a valid name"})

    # Using uuid4 to generate token because
    # it's a publicly available endpoint
    token = str(uuid.uuid4())

    # Simple dictionary for name & token
    data = {"name": name, "token": token}

    return data

# @route    POST /refresh_token
# @desc     Route to refresh token
# @access   Public


@chat.post("/refresh_token")
async def refresh_token(request: Request):
    return None

# @route    Websocket /chat
# @desc     Socket for chatbot
# @access   Public


@chat.websocket("/chat")
# Take a WebSocket and add to connection manager
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        # Run a while True loop to ensure socket stays open
        while True:
            # Receive any messages sent by client and print to terminal for now
            data = await websocket.receive_text()
            print(data)
            await manager.send_personal_message(f"Response: Simulating response from the GPT service", websocket)

    # Except when the socket gets disconnected
    except WebSocketDisconnect:
        manager.disconnect(websocket)