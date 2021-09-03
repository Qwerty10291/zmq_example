import asyncio
from servers.pubsub import PubSubServer
from datetime import datetime


async def main():
    while True:
        await server.send_data('any', datetime.now())
        await asyncio.sleep(0.01)

loop = asyncio.get_event_loop()
server = PubSubServer(loop)
loop.run_until_complete(main())