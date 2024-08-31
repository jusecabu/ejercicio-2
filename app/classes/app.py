from category import Category
from supplier import Supplier
from product import Product
from storage import Storage

class App:
    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.suppliers: list[Supplier] = []
        self.storages: list[Storage] = []
        self.products: list[Product] = []
        pass