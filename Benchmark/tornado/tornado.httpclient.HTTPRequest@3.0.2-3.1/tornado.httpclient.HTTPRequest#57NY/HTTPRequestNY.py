import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get',  'GET',  {'Content-Type': 'application/json'},  None,  None,  None,  20,  20, if_modified_since=None, follow_redirects=True)
