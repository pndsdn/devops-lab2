from src.snp import StringFormingRequestHandler
def string_forming(self: StringFormingRequestHandler) -> None:
    message = self.get_argument('message')
    while '  ' in message:
        message.replace('  ', ' ')

    while (ord(message[0]) < 65 or ord(message[0]) > 90) \
            and (ord(message[0]) < 97 or ord(message[0]) > 122):
        message.replace(message[0], '')

    message = f'{message[0].capitalize()}{message[1:]}'

    ch = 0
    while ch + 2 != len(message):
        if message[ch] in '.!?':
            if message[ch + 1] != ' ':
                message = f'{message[:ch + 1]} ' \
                          f'{message[ch + 1].capitalize()}{message[ch + 2:]}'

            if message[ch - 1] == ' ':
                message = f'{message[:ch - 1]}{message[ch:]}'

        if message[ch] in ',:':
            if message[ch + 1] != ' ':
                message = f'{message[:ch + 1]} {message[ch + 1:]}'

            if message[ch - 1] == ' ':
                message = f'{message[:ch - 1]}{message[ch:]}'

        ch += 1

    if message[len(message) - 1] not in '.!?':
        message = f'{message}.'

    self.write(message)
