import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', method='GET')
