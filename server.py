#!/usr/bin/python
import sys
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import template
import logging 

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = template.Loader("/home/ccheng/workspace_tb/tornado_pushtool")
        self.write(loader.load("index.html").generate())

class LoadingHandler(tornado.web.RequestHandler):
    def get(self):
        sys.stderr.write("argument:" + self.get_argument("ip") + "\n")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/loading", LoadingHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
