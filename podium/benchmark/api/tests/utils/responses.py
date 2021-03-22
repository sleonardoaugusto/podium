import requests
import vcr


@vcr.use_cassette('podium/benchmark/api/tests/fixtures/vcr_cassettes/get_items.yaml')
def item_list(query_params={}):
    url = 'https://api.mercadolibre.com/sites/MLA/search'
    params = {'category': 'MLA420040', 'sort': 'sold_quantity_desc', 'offset': 1}
    q = {**params, **query_params}
    resp = requests.get(url, params=q)
    items = resp.json()['results']
    return items


def item_detail():
    items = item_list()
    return items[13]


def seller_detail():
    item = item_detail()
    return item['seller']
