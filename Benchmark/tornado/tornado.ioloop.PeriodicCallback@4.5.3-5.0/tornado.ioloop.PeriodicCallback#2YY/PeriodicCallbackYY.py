import tornado.ioloop

def my_callback():
    print('Hello, Tornado!')
tornado.ioloop.PeriodicCallback(my_callback, callback_time=1000)
