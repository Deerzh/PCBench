import aiohttp
from aiohttp import web
import logging
app = web.Application(router=None, loop=None, logger=logging.getLogger(__name__))
