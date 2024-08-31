from category import Category

class Product:
    def __init__(self, name: str, description: str, price: int, stock: int, category: Category) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category.name
        pass