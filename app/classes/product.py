from category import Category

class Product:
    def __init__(self, name: str, description: str, price: int, stock: int, category: Category) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category.name

    def add_to_stock(self, quantity: int):
        pass

    def remove_from_stock(self, quantity: int):
        pass

    def get_value_from_stock(self):
        pass