import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get',  'GET',  {'Content-Type': 'application/json'},  None, auth_username=None, auth_password=None)
