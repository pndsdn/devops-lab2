from funcional import nameFormating, stringFormating

import tornado.ioloop
import tornado.web


class nameRequestHandler(tornado.web.RequestHandler):
    def get(self):
        nameFormating(self)


class stringFormatingRequestHandler(tornado.web.RequestHandler):
    def get(self):
        stringFormating(self)


app = tornado.web.Application([
    (r'/user', nameRequestHandler),
    (r'/write', stringFormatingRequestHandler)
])

if __name__ == '__main__':
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()
