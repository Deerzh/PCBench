import tornado.escape
value_to_unescape = 'hello world'
unescaped_value = tornado.escape.url_unescape(value=value_to_unescape)
print(unescaped_value)
