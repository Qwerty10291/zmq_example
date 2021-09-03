import asyncio
from typing import Dict
from clients.handler import Handler
import zmq
import zmq.asyncio
from .client import Client

class PubSubClient(Client):
    def __init__(self, loop, ip, port) -> None:
        super().__init__(loop)

        self.socket = self.ctx.socket(zmq.SUB)
        self.socket.connect(f'tcp://{ip}:{port}')
        self.socket.subscribe('')

        self.topic_handlers :Dict[str, Handler] = {}
    
    def add_topic_handler(self, name, func, is_async=False):
        self.topic_handlers[name] = Handler(self, name, func, is_async)
    
    def start(self):
        asyncio.ensure_future(self.start_polling(), self.loop)
    
    async def start_polling(self):
        while True:
            message = await self.socket.recv_pyobj()
            if isinstance(message, dict):
                topic_name = message.pop('topic')
                if topic_name in self.topic_handlers:
                    self.topic_handlers[topic_name].run(message['data'])