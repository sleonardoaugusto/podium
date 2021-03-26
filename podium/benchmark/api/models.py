class Model:
    @property
    def serialized(self):
        read_only = ['pk']
        d = {}

        for k, v in self.__dict__.items():
            if k not in read_only:
                d.update({k: v})

        return d


class Seller(Model):
    def __init__(self, pk: int, nickname: str):
        self.pk = pk
        self.nickname = nickname


class Item(Model):
    def __init__(self, pk: int, title: str, price: float, link: str):
        self.pk = pk
        self.title = title
        self.price = price
        self.link = link
