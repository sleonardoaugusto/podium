from podium.benchmark.api import SellerParser


class SellerSearcher:
    SORT = 'sold_quantity_desc'
    CATEGORY = 'MLA420040'
    LIMIT = 10

    def __init__(self, api_client, category: str = None, limit: int = None):
        self.parser = SellerParser()
        self.client = api_client
        self.category = category or self.CATEGORY
        self.limit = limit or self.LIMIT

    def get_best_sellers(self, offset):
        q = {'category': self.category, 'sort': self.SORT, 'offset': offset}
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
            sellers = self.get_best_sellers(offset)

            for s in sellers:
                seller = self.parser.parse(s['seller'])

                if self.must_add(best_sellers, seller.pk):
                    best_sellers.append(seller)

                if len(best_sellers) == self.limit:
                    break

            offset += 1

        return best_sellers
