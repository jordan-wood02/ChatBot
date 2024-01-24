from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        # List of all active connections
        self.active_connections: list[WebSocket] = []

    # Accept WebSocket and add to list of active connections
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # Remove WebSocket from list of active connections
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # Take in a message and the WebSocket we want to send message to
    # and asynchronously send the message
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)