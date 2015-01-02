import os
from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class IndexHandler(BaseHandler):
    def req(self):
        super(IndexHandler,self).req()
        # self.write(os.path.dirname(os.path.realpath(__file__)))
        self.render("home/index.html")
        self.finish()
