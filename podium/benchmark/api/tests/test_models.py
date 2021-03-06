from django.test import TestCase

from podium.benchmark.api import Seller, Item


class SellerTest(TestCase):
    def setUp(self) -> None:
        self.seller = Seller(1, 'Adalberto')

    def test_init(self):
        self.assertEqual(self.seller.pk, 1)
        self.assertEqual(self.seller.nickname, 'Adalberto')


class ItemTest(TestCase):
    def setUp(self) -> None:
        self.item = Item(1, 'Funda Power Case Soul', 4499, 'https://fundapower.com')

    def test_init(self):
        self.assertEqual(self.item.pk, 1)
        self.assertEqual(self.item.title, 'Funda Power Case Soul')
        self.assertEqual(self.item.price, 4499)
        self.assertEqual(self.item.link, 'https://fundapower.com')


class ModelTest(TestCase):
    def setUp(self) -> None:
        self.seller = Seller(1, 'Adalberto')
        self.item = Item(1, 'Funda Power Case Soul', 4499, 'https://fundapower.com')

    def test_serialized(self):
        serializers = (
            (self.seller, {'nickname': self.seller.nickname}),
            (
                self.item,
                {
                    'title': self.item.title,
                    'price': self.item.price,
                    'link': self.item.link,
                },
            ),
        )
        for model, expect in serializers:
            with self.subTest():
                self.assertEqual(model.serialized, expect)
