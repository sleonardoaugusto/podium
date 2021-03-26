from django.shortcuts import render

from podium.benchmark.api import APIClient, SellerParser
from podium.benchmark.api.parsers import ItemParser
from podium.benchmark.api.searchers import Searcher


def parse_params(request):
    expected_params = ['category', 'limit']
    q = {}

    for p in expected_params:
        value = request.GET.get(p)

        if p == 'limit' and value:
            value = int(value)

        q.update({p: value})

    return q


def best_sellers(request):
    params = parse_params(request)
    api_client = APIClient()
    parser = SellerParser()
    items = Searcher(api_client, parser, **params).run()

    return render(request, 'benchmark/sellers.html', {'sellers': items})


def expensive_items(request):
    params = parse_params(request)
    api_client = APIClient()
    parser = ItemParser()
    items = Searcher(api_client, parser, **params).run()

    return render(request, 'benchmark/items.html', {'items': items})
