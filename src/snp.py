from src.funcional import string_forming

import tornado.ioloop
import tornado.web


class StringFormingRequestHandler(tornado.web.RequestHandler):
    def get(self) -> None:
        string_forming(self)


def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r'/write', StringFormingRequestHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
