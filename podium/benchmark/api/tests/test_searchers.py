from unittest.mock import patch, call, MagicMock

from django.test import TestCase

from podium.benchmark.api import APIClient, Seller, SellerParser, Searcher, Item
from podium.benchmark.api.parsers import ItemParser


class SearcherTest(TestCase):
    def setUp(self) -> None:
        self.searcher = Searcher(APIClient(), MagicMock())

    def test_init(self):
        self.assertTrue(self.searcher)
        self.assertIsInstance(self.searcher.client, APIClient)
        self.assertEqual(self.searcher.category, 'MLA420040')
        self.assertEqual(self.searcher.limit, 10)

    @patch('podium.benchmark.api.client.APIClient.get_item_list')
    def test_get_items(self, mock):
        mock.return_value = {}
        resp = self.searcher.get_items(1)

        self.assertEqual(resp, {})
        mock.assert_called_once_with(
            {
                'category': self.searcher.category,
                'sort': self.searcher.sort,
                'offset': 1,
            }
        )

    def test_must_not_add(self):
        sellers = [Seller(pk=1, nickname='')]
        self.assertFalse(self.searcher.must_add(sellers, pk=1))

    def test_must_add(self):
        sellers = [Seller(pk=1, nickname='')]
        self.assertTrue(self.searcher.must_add(sellers, pk=2))


class SearcherSellerTest(TestCase):
    def setUp(self) -> None:
        self.searcher = Searcher(APIClient(), SellerParser())

    def test_init(self):
        self.assertEqual(self.searcher.sort, Searcher.SELLER_SORT)

    @patch('podium.benchmark.api.searchers.Searcher.get_items')
    @patch('podium.benchmark.api.searchers.Searcher.must_add')
    @patch('podium.benchmark.api.parsers.SellerParser.parse')
    def test_run(self, mock_parse, mock_add, mock_get):
        per_page, pages = 11, 3

        mock_get.side_effect = [[{'seller': {}}] * per_page] * pages
        mock_add.return_value = True
        mock_parse.return_value = Seller(0, '')

        sellers = self.searcher.run()

        mock_parse.assert_has_calls([call({})] * self.searcher.limit)
        self.assertEqual(len(sellers), 10)


class SearcherItemTest(TestCase):
    def setUp(self) -> None:
        self.searcher = Searcher(APIClient(), ItemParser())

    def test_init(self):
        self.assertEqual(self.searcher.sort, Searcher.ITEM_SORT)

    @patch('podium.benchmark.api.searchers.Searcher.get_items')
    @patch('podium.benchmark.api.searchers.Searcher.must_add')
    @patch('podium.benchmark.api.parsers.ItemParser.parse')
    def test_run(self, mock_parse, mock_add, mock_get):
        per_page, pages = 11, 3

        mock_get.side_effect = [[{'seller': {}}] * per_page] * pages
        mock_add.return_value = True
        mock_parse.return_value = Item(0, '', 0.0, '')

        sellers = self.searcher.run()

        mock_parse.assert_has_calls([call({'seller': {}})] * self.searcher.limit)
        self.assertEqual(len(sellers), 10)
