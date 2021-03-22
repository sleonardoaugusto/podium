from unittest import TestCase
from unittest.mock import patch

from podium.benchmark.api import APIClient, Seller
from podium.benchmark.api.searchers import SellerSearcher


class SellerSearcherTest(TestCase):
    def setUp(self) -> None:
        self.searcher = SellerSearcher(APIClient, 'MLA420040', 'sold_quantity_desc')

    def test_init(self):
        self.assertTrue(self.searcher)
        self.assertIsInstance(APIClient(), self.searcher.client)
        self.assertEqual(self.searcher.category, 'MLA420040')
        self.assertEqual(self.searcher.sort, 'sold_quantity_desc')
        self.assertEqual(self.searcher.limit, 10)

    @patch('podium.benchmark.api.client.APIClient.get_item_list')
    def test_get_best_sellers(self, mock):
        mock.return_value = {}
        resp = self.searcher.get_best_sellers(1)

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

    @patch('podium.benchmark.api.searchers.SellerSearcher.get_best_sellers')
    @patch('podium.benchmark.api.searchers.SellerSearcher.must_add')
    @patch('podium.benchmark.api.searchers.SellerParser.parse')
    def test_run(self, mock_parse, mock_add, mock_get):
        per_page, pages = 11, 3

        mock_get.side_effect = [[{'seller': {}}] * per_page] * pages
        mock_add.return_value = True
        mock_parse.return_value = Seller(pk=0, nickname='')

        sellers = self.searcher.run()

        self.assertEqual(len(sellers), 10)
