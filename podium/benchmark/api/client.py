import requests


class APIClient:
    URL = 'https://api.mercadolibre.com/sites/MLA/search'

    def __init__(self):
        self.client = requests

    @staticmethod
    def _to_querystring(params: dict):
        q = ''

        if params:
            for k, v in params.items():
                separator = '?' if '?' not in q else '&'
                querystring = f'{k}={v}'
                q = separator.join([q, querystring])

        return q

    def build_url(self, query_params):
        q = self._to_querystring(query_params)
        url = f'{self.URL}{q}'
        return url

    def get_item_list(self, query_params: dict):
        url = self.build_url(query_params)
        resp = self.client.get(url)
        return resp.json()['results']
