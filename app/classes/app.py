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

    def get_product_info(self, product: Product):
        pass

    def get_category_info(self, category: Category):
        pass

    def get_storage_info(self, storage: Storage):
        pass

    def get_supplier_info(self, supplier: Supplier):
        pass

    def get_stock_info(self):
        pass