from product import Product

class Storage:
    def __init__(self, name: str, location: str, maximum_capacity: int, stored_products: list[Product]) -> None:
        self.name = name
        self.location = location
        self.maximum_capacity = maximum_capacity
        self.stored_products = stored_products

    def add_product(self, product: Product):
        pass

    def remove_product(self, product: Product):
        pass

    def find_product(self, product: Product):
        pass