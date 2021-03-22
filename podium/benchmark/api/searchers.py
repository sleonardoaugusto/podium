from podium.benchmark.api import SellerParser


class SellerSearcher:
    def __init__(self, api_client, category, sort, limit=10):
        self.parser = SellerParser()
        self.client = api_client
        self.category = category
        self.sort = sort
        self.limit = limit

    def get_best_sellers(self, offset):
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
            sellers = self.get_best_sellers(offset)

            i = 0
            for s in sellers:
                seller = self.parser.parse(s['seller'])
                i += 1
                print(i, seller)

                if self.must_add(best_sellers, seller.pk):
                    best_sellers.append(seller)

                    if len(best_sellers) == self.limit:
                        break

            offset += 1

        return best_sellers
