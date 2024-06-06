import requests
cookie_jar = requests.cookies.RequestsCookieJar()
cookie_jar.set('cookie1', 'value1', domain='example.com', path='/')
cookie_jar.set('cookie2', 'value2', domain='example.com', path='/subpath')
retrieved_cookie = cookie_jar.get(name='cookie1', domain='example.com', path='/')
print('Retrieved Cookie:', retrieved_cookie)
