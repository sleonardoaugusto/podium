from django.test import TestCase

from podium.benchmark.api import SellerParser
from podium.benchmark.api.parsers import ItemParser


class SellerParserTest(TestCase):
    def setUp(self) -> None:
        self.parser = SellerParser()

    def test_init(self):
        self.assertTrue(self.parser)

    def test_parse(self):
        item = {
            'seller': {
                'id': 1,
                'permalink': 'http://perfil.mercadolibre.com.ar/SUPER_SHOP',
            }
        }
        parsed = self.parser.parse(item['seller'])

        values = (
            (parsed.pk, 1),
            (parsed.nickname, 'SUPER_SHOP'),
        )
        for value, expect in values:
            with self.subTest():
                self.assertEqual(value, expect)


class ItemParserTest(TestCase):
    def setUp(self) -> None:
        self.parser = ItemParser()

    def test_init(self):
        self.assertTrue(self.parser)

    def test_parse(self):
        item = {
            'id': 1,
            'title': 'my title',
            'price': 0,
            'permalink': 'http://perfil.mercadolibre.com.ar/ITEM',
        }
        parsed = self.parser.parse(item)

        values = (
            (parsed.title, 'my title'),
            (parsed.price, 0),
            (parsed.link, 'http://perfil.mercadolibre.com.ar/ITEM'),
        )
        for value, expect in values:
            with self.subTest():
                self.assertEqual(value, expect)
