import requests
import vcr
from django.test import TestCase

from podium.benchmark.api import APIClient


class APIClientTest(TestCase):
    def setUp(self) -> None:
        self.url = 'https://api.mercadolibre.com'
        self.site = 'MLA'
        self.query_params = {
            'category': 'MLA420040',
            'sort': 'sold_quantity_desc',
            'offset': 1,
        }
        self.api_client = APIClient()

    def test_init(self):
        self.assertEqual(self.api_client.client, requests)

    def test_to_querystring(self):
        """Must convert dict structure to querystring"""
        q = self.api_client._to_querystring(self.query_params)
        expect = '?category=MLA420040&sort=sold_quantity_desc&offset=1'

        self.assertEqual(q, expect)

    def test_build_url(self):
        url = self.api_client.build_url(self.query_params)
        self.assertEqual(
            url,
            'https://api.mercadolibre.com/sites/MLA/search?category=MLA420040&sort=sold_quantity_desc&offset=1',
        )

    @vcr.use_cassette(
        'podium/benchmark/api/tests/fixtures/vcr_cassettes/item_list.yaml'
    )
    def test_get_item_list(self):
        items = self.item_list(self.query_params)
        resp = self.api_client.get_item_list(self.query_params)
        self.assertEqual(resp, items)

    @staticmethod
    @vcr.use_cassette(
        'podium/benchmark/api/tests/fixtures/vcr_cassettes/get_items.yaml'
    )
    def item_list(query_params=None):
        if query_params is None:
            query_params = {}

        url = 'https://api.mercadolibre.com/sites/MLA/search'
        params = {'category': 'MLA420040', 'sort': 'sold_quantity_desc', 'offset': 1}
        q = {**params, **query_params}
        resp = requests.get(url, params=q)
        items = resp.json()['results']
        return items
