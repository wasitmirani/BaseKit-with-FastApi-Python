from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket.manager import manager

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room: str):
    await manager.connect(room, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.broadcast(room, {"room": room, "data": data})
    except WebSocketDisconnect:
        manager.disconnect(room, websocket)
