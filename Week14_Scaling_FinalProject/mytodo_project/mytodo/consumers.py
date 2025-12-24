from channels.generic.websocket import AsyncWebsocketConsumer

class TodoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="WebSocket connection established.")
        

