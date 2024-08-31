from product import Product

class Supplier:
    def __init__(self, name: str, direction: str, phone: str, supplied_products: list[Product]) -> None:
        self.name = name
        self.direction = direction
        self.phone = phone
        self.supplied_products = supplied_products
        pass