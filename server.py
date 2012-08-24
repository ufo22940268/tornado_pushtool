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

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
