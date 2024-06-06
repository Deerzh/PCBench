import tornado.httpclient
import tornado.ioloop

async def fetch_url():
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = await http_client.fetch(request='http://example.com', callback=None, raise_error=True)
tornado.ioloop.IOLoop.current().run_sync(fetch_url)
