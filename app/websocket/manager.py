from typing import Any

from fastapi import WebSocket


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, room: str, websocket: WebSocket) -> None:
        await websocket.accept()
        self.active_connections.setdefault(room, []).append(websocket)

    def disconnect(self, room: str, websocket: WebSocket) -> None:
        if room in self.active_connections:
            self.active_connections[room] = [
                conn for conn in self.active_connections[room] if conn != websocket
            ]

    async def broadcast(self, room: str, message: dict[str, Any]) -> None:
        for connection in self.active_connections.get(room, []):
            await connection.send_json(message)


manager = ConnectionManager()
