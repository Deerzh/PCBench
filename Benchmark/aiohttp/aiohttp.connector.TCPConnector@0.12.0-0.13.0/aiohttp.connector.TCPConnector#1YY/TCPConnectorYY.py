import aiohttp
import asyncio

async def fetch_page(url, loop):
    connector = aiohttp.TCPConnector()
    response = await aiohttp.request('GET', url, connector=connector)
    raw_response = await response.read()
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('http://example.com', loop))
