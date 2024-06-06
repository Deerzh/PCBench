import asyncio
import aiohttp
from aiohttp import CookieJar
from aiohttp.client_reqrep import ClientRequest, ClientResponse
from aiohttp.client_ws import ClientWebSocketResponse
from aiohttp import HttpVersion

async def main():
    cookies = {'test': 'cookie_value'}
    headers = {'Content-Type': 'application/json'}
    skip_auto_headers = {'User-Agent'}
    auth = aiohttp.BasicAuth('user', 'pass')
    request_class = ClientRequest
    response_class = ClientResponse
    ws_response_class = ClientWebSocketResponse
    cookie_jar = CookieJar()
    read_timeout = 10
    session = aiohttp.ClientSession(version=HttpVersion(major=1, minor=1), request_class=request_class, loop=None, skip_auto_headers=skip_auto_headers, headers=headers, cookies=cookies, cookie_jar=cookie_jar, ws_response_class=ws_response_class, connector=None, response_class=response_class, read_timeout=read_timeout, auth=auth)
    response = await session.get('http://httpbin.org/get')
    data = await response.text()
    print(data)
    await session.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
