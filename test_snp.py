import pytest
import tornado
from tornado.httpclient import HTTPClient, AsyncHTTPClient


def fetch(url):
    client = HTTPClient()
    response = client.fetch(url)
    return response.body.decode()


def test_snp():
    assert fetch('http://127.0.0.1:8080/user?name=andrew') == 'Hello, Andrew!'
    assert fetch('http://127.0.0.1:8080/write?message=one,%20two,three,four%20,five-I%60m%20going%20to%20look%21') \
           == 'One, two, three, four, five - I`m going to look!'
    assert fetch('http://127.0.0.1:8080/write?message=this%20is%20mine%20message.') == 'This is mine message.'
    assert fetch('http://127.0.0.1:8080/write?message=first%20sentence.second%20sentence%20.third%20sentence') \
           == 'First sentence. Second sentence. Third sentence.'


test_snp()
