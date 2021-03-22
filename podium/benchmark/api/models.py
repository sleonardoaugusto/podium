class Seller:
    def __init__(self, pk: int, nickname: str):
        self.pk = pk
        self.nickname = nickname


class Item:
    def __init__(self, title: str, price: int, link: str):
        self.title = title
        self.price = price
        self.link = link
