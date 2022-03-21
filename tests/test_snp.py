from abc import ABC
from collections import namedtuple

import tornado.web
from tornado.testing import AsyncHTTPTestCase

from src import snp


class TestSnpApp(AsyncHTTPTestCase, ABC):
    def get_app(self) -> tornado.web.Application:
        return snp.make_app()

    def test_message_request(self):
        positive_case = namedtuple("positive_case", ["value", "expected"])
        test_table = [
            positive_case('one,%20two%20,three%20,four,%20five.I`m%20going%20to%20look%21',
                          'One, two, three, four, five. I`m going to look!'),
            positive_case('this%20is%20mine%20message.', 'This is mine message.'),
            positive_case('first%20sentence.second%20sentence%20.third%20sentence',
                          'First sentence. Second sentence. Third sentence.')
        ]

        for test_case in test_table:
            response = self.fetch(f"/write?message={test_case.value}")
            self.assertEqual(response.code, 200)
            self.assertEqual(response.body.decode(), test_case.expected)
