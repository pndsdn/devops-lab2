import tornado.ioloop
import tornado.web


class nameRequestHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name')
        self.write(f'Hello, {name[0].capitalize()}{name[1:]}!')


class stringFormatingRequestHandler(tornado.web.RequestHandler):
    def get(self):
        message = self.get_argument('message')
        while '  ' in message:
            message.replace('  ', ' ')

        while (ord(message[0]) < 65 or ord(message[0]) > 90) and (ord(message[0]) < 97 or ord(message[0]) > 122):
            message.replace(message[0], '')

        message = f'{message[0].capitalize()}{message[1:]}'

        ch = 0
        while ch + 2 != len(message):
            if message[ch] in '.!?':
                if message[ch+1] != ' ':
                    message = f'{message[:ch + 1]} {message[ch +1 ].capitalize()}{message[ch + 2:]}'

                if message[ch-1] == ' ':
                    message = f'{message[:ch - 1]}{message[ch:]}'

            if message[ch] in ',:':
                if message[ch+1] != ' ':
                    message = f'{message[:ch + 1]} {message[ch + 1:]}'

                if message[ch-1] == ' ':
                    message = f'{message[:ch - 1]}{message[ch:]}'

            if message[ch] == '-':
                if message[ch+1] != ' ':
                    message = f'{message[:ch + 1]} {message[ch + 1:]}'

                if message[ch-1] != ' ':
                    message = f'{message[:ch]} {message[ch:]}'

            ch += 1

        if message[len(message)-1] not in '.!?':
            message = f'{message}.'

        self.write(message)


app = tornado.web.Application([
    (r'/user', nameRequestHandler),
    (r'/write', stringFormatingRequestHandler)
])

if __name__ == '__main__':
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
