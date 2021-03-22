from django.shortcuts import render

from podium.benchmark.api import APIClient
from podium.benchmark.api.searchers import SellerSearcher


def best_sellers(request):
    api_client = APIClient()
    items = SellerSearcher(api_client, 'MLA420040', 'sold_quantity_desc').run()
    return render(request, 'benchmark/sellers.html', {'sellers': items})
