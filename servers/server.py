import asyncio
import zmq.asyncio
import zmq

class Server:
    def __init__(self, loop) -> None:
        if not hasattr(Server, 'ctx'):
            Server.ctx = zmq.asyncio.Context()
        self.loop = loop
