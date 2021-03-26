from podium.benchmark.api import SellerParser


class Searcher:
    SELLER_SORT = 'sold_quantity_desc'
    ITEM_SORT = 'price_desc'
    CATEGORY = 'MLA420040'
    LIMIT = 10

    def __init__(self, api_client, parser, category: str = None, limit: int = None):
        self.client = api_client
        self.parser = parser
        self.category = category or self.CATEGORY
        self.limit = limit or self.LIMIT
        self.sort = self._get_sort()

    def _get_sort(self):
        if isinstance(self.parser, SellerParser):
            return self.SELLER_SORT
        return self.ITEM_SORT

    def get_items(self, offset):
        q = {'category': self.category, 'sort': self.sort, 'offset': offset}
        resp = self.client.get_item_list(q)
        return resp

    @staticmethod
    def must_add(items, pk):
        ids = map(lambda x: x.pk, items)
        return pk not in ids

    def run(self):
        offset = 1
        best_sellers = []

        while len(best_sellers) < self.limit:
            sellers = self.get_items(offset)

            for s in sellers:

                if isinstance(self.parser, SellerParser):
                    seller = self.parser.parse(s['seller'])
                else:
                    seller = self.parser.parse(s)

                if self.must_add(best_sellers, seller.pk):
                    best_sellers.append(seller)

                if len(best_sellers) == self.limit:
                    break

            offset += 1

        return best_sellers
