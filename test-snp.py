from tornado.httpclient import HTTPClient


def fetch(url):
    client = HTTPClient()
    response = client.fetch(url)
    return response.body.decode()


assert fetch('http://127.0.0.1:8080/user?name=andrew') == 'Hello, Andrew'
assert fetch('http://127.0.0.1:8080/write?message=this%20is%20mine%20message') == 'This is mine message'
assert fetch('http://127.0.0.1:8080/write?message=first%20sentence.second%20sentence') == 'First sentence. ' \
                                                                                          'Second sentence'
