from product import Product

class Category:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.products: list[Product] = []
        pass