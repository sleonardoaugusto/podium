class Seller:
    def __init__(self, pk: int, nickname: str):
        self.pk = pk
        self.nickname = nickname


class Item:
    def __init__(self, pk: int, title: str, price: float, link: str):
        self.pk = pk
        self.title = title
        self.price = price
        self.link = link
