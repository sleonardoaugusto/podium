from django.test import TestCase

from podium.benchmark.api import SellerParser
from podium.benchmark.api.parsers import ItemParser
from podium.benchmark.api.tests.utils import responses


class SellerParserTest(TestCase):
    def setUp(self) -> None:
        self.parser = SellerParser()
        self.response = responses.seller_detail()

    def test_init(self):
        self.assertTrue(self.parser)

    def test_parse(self):
        parsed = self.parser.parse(self.response)

        values = (
            (parsed.pk, self.response['id']),
            (
                parsed.nickname,
                self.response['permalink']
                .split('http://perfil.mercadolibre.com.ar/')[1]
                .replace('+', ' '),
            ),
        )
        for value, expect in values:
            with self.subTest():
                self.assertEqual(value, expect)


class ItemParserTest(TestCase):
    def setUp(self) -> None:
        self.parser = ItemParser()
        self.response = responses.item_detail()

    def test_init(self):
        self.assertTrue(self.parser)

    def test_parse(self):
        parsed = self.parser.parse(self.response)

        values = (
            (parsed.title, self.response['title']),
            (parsed.price, self.response['price']),
            (parsed.link, self.response['permalink']),
        )
        for value, expect in values:
            with self.subTest():
                self.assertEqual(value, expect)
