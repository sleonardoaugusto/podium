from django.shortcuts import render

from podium.benchmark.api import APIClient
from podium.benchmark.api.searchers import SellerSearcher


def best_sellers(request):
    def parse_params():
        expected_params = ['category', 'limit']
        q = {}

        for p in expected_params:
            value = request.GET.get(p)

            if p == 'limit' and value:
                value = int(value)

            q.update({p: value})

        return q

    params = parse_params()
    api_client = APIClient()
    items = SellerSearcher(api_client, **params).run()
    return render(request, 'benchmark/sellers.html', {'sellers': items})
