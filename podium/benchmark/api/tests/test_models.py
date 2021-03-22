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
        self.item = Item('Funda Power Case Soul', 4499, 'https://fundapower.com')

    def test_init(self):
        self.assertEqual(self.item.title, 'Funda Power Case Soul')
        self.assertEqual(self.item.price, 4499)
        self.assertEqual(self.item.link, 'https://fundapower.com')
