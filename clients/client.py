import zmq
import zmq.asyncio
import asyncio
class Client:
    def __init__(self, loop) -> None:
        if not hasattr(Client, 'ctx'):
            Client.ctx = zmq.asyncio.Context()
        self.loop = loop
    