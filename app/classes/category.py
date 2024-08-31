from product import Product

class Category:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.products: list[Product] = []

    def add_product(self, product: Product):
        pass

    def remove_product(self, product: Product):
        pass