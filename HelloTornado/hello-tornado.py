#!/usr/bin/python
'''hello-tornado.py'''
# pip install tornado
import logging

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options



class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish('hello world!')


class Application(tornado.web.Application):
    def __init__(self):
        app_settings = {'debug': True}

        app_handlers = [
            (r'^/', HelloWorldHandler)
        ]
        super(Application, self).__init__(app_handlers, app_settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()

    port = 3030
    address = '0.0.0.0'
    http_server = tornado.httpserver.HTTPServer(
        request_callback=Application(),
        xheaders=True
    )
    http_server.listen(port, address=address)
    tornado.ioloop.IOLoop.instance().start()


## add a post
