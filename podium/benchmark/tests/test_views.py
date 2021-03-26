from unittest.mock import patch

from django.test import TestCase

from podium.benchmark.api import Seller, Item


class SellersViewTest(TestCase):
    def setUp(self) -> None:
        self.resp = self.get()

    def get(self, q='', item=Seller(pk=0, nickname='')):
        with patch('podium.benchmark.views.Searcher.run') as mock:
            mock.return_value = [item]
            resp = self.client.get(f'/best-sellers/{q}')
            return resp

    def test_get(self):
        """GET /best-sellers/ must return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Page must render sellers.html template"""
        self.assertTemplateUsed(self.resp, 'benchmark/sellers.html')

    def test_template_context(self):
        context = self.resp.context['sellers']
        self.assertEqual(len(context), 1)

    def test_html(self):
        item = Seller(pk=0, nickname='Pombinha Guerreira Martins')
        resp = self.get(item=item)
        self.assertContains(resp, item.nickname)


class ItemViewTest(TestCase):
    def setUp(self) -> None:
        self.resp = self.get()

    def get(self, q='', item=Item(0, '', 0, '')):
        with patch('podium.benchmark.views.Searcher.run') as mock:
            mock.return_value = [item]
            resp = self.client.get(f'/expensive-items/{q}')
            return resp

    def test_get(self):
        """GET /expensive-items/ must return status code 200"""
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """Page must render sellers.html template"""
        self.assertTemplateUsed(self.resp, 'benchmark/items.html')

    def test_template_context(self):
        context = self.resp.context['items']
        self.assertEqual(len(context), 1)

    def test_html(self):
        item = Item(pk=1, title='Some title', price=999.99, link='http://mylink.com')
        resp = self.get(item=item)
        self.assertContains(resp, item.title)
        self.assertContains(resp, item.price)
        self.assertContains(resp, item.link)
