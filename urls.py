from handlers.foo import FooHandler
from handlers.index import IndexHandler
from tornado.web import StaticFileHandler
url_patterns = [
    (r"/foo", FooHandler),
    (r"/index", IndexHandler),
    (r"/", IndexHandler),

]
