import asyncio
from clients.sub import PubSubClient


def time_handler(time):
    print(time)

loop = asyncio.get_event_loop()
client = PubSubClient(loop, '127.0.0.1', '5000')
client.add_topic_handler('any', time_handler)
loop.run_until_complete(client.start_polling())