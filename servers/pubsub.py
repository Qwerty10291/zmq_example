from .server import Server
import zmq


class PubSubServer(Server):
    def __init__(self, loop, port=5000) -> None:
        super().__init__(loop)
        self.socket = self.ctx.socket(zmq.PUB)
        self.socket.bind(f'tcp://*:{port}')
    
    async def send_data(self, topic:str, data):
        message = {'topic': topic,
                  'data': data}
        await self.socket.send_pyobj(message)