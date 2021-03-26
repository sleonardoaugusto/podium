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
    def parse(self, obj):
        i = Item(
            pk=self.extract_id(obj),
            title=self.extract_title(obj),
            price=self.extract_price(obj),
            link=self.extract_link(obj),
        )
        return i

    @staticmethod
    def extract_id(obj):
        return obj['id']

    @staticmethod
    def extract_title(obj):
        return obj['title']

    @staticmethod
    def extract_price(obj):
        return obj['price']

    @staticmethod
    def extract_link(obj):
        return obj['permalink']
