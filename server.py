#!/usr/bin/python
import sys
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import template
import logging 
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = template.Loader("/Users/ccheng/workspace_tb/tornado_pushtool")
        self.write(loader.load("index.html").generate())

class LoadingHandler(tornado.web.RequestHandler):
    def get(self):
        sys.stderr.write("argument:" + self.get_argument("ip") + "\n")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        pass

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "js"),
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/loading", LoadingHandler),
    (r"/ajaxTesting", TestHandler),
], **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
