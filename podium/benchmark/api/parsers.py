from .models import Seller, Item


class SellerParser:
    def parse(self, data):
        s = Seller(
            pk=self.extract_id(data),
            nickname=self.extract_nickname(data),
        )
        return s

    @staticmethod
    def extract_id(data):
        return data['id']

    @staticmethod
    def extract_nickname(data):
        nickname = data['permalink'].split('http://perfil.mercadolibre.com.ar/')[1]
        return nickname.replace('+', ' ')


class ItemParser:
    def parse(self, data):
        i = Item(
            title=self.extract_title(data),
            price=self.extract_price(data),
            link=self.extract_link(data),
        )
        return i

    @staticmethod
    def extract_title(data):
        return data['title']

    @staticmethod
    def extract_price(data):
        return data['price']

    @staticmethod
    def extract_link(data):
        return data['permalink']
