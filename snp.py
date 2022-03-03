import tornado.ioloop
import tornado.web


class nameRequestHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name')
        self.write(f'Hello, {name[0].capitalize()}{name[1:]}')


class stringFormatingRequestHandler(tornado.web.RequestHandler):
    def get(self):
        message = self.get_argument('message')
        while '  ' in message:
            message.replace('  ', ' ')

        while (ord(message[0]) < 65 or ord(message[0]) > 90) and (ord(message[0]) < 97 or ord(message[0]) > 122):
            message.replace(message[0], '')

        message = f'{message[0].capitalize()}{message[1:]}'

        for ch in message:
            if ch in '.!?':
                message = f'{message[:message.index(ch)+1]} {message[message.index(ch)+1].capitalize()}' \
                          f'{message[message.index(ch)+2:]}'

        self.write(message)


app = tornado.web.Application([
    (r'/user', nameRequestHandler),
    (r'/write', stringFormatingRequestHandler)
])

if __name__ == '__main__':
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
