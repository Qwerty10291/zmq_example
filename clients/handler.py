from .client import Client
import asyncio

class Handler:
    def __init__(self, parent:Client, name, func, is_async=False) -> None:
        self.parent = parent
        self.name = name
        self.func = func
        self.is_async = is_async
    
    def run(self, data):
        if self.is_async:
            asyncio.ensure_future(self.func(data), self.parent.loop)
        else:
            self.func(data)
