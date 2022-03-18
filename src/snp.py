from src.funcional import StringForming

import tornado.ioloop
import tornado.web


class StringFormingRequestHandler(tornado.web.RequestHandler):
    def get(self):
        StringForming(self)


def make_app():
    app = tornado.web.Application([
        (r'/write', StringFormingRequestHandler)
    ])

    if __name__ == '__main__':
        app.listen(8080)
        tornado.ioloop.IOLoop.current().start()

