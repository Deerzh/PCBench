from aiohttp import web
app = web.Application()
app.router.add_static('/static/',  '/home/zhang/aiohttp', name='static', expect_handler=None)
