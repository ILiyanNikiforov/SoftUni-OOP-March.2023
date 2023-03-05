from project.product import Product


class ProductRepository():

    def __init__(self):
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [Product, None]:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name) -> None:
        # ProductRepository.products.remove(product_name) if product_name in ProductRepository.products else None
        product = self.find(product_name)

        if product:
            self.products.remove(product)
        # self.products.remove(self.find(product)) if product is not None else None


    def __repr__(self):
        # result = []
        # for product in self.products:
        #     result.append(f"{product.name}: {product.quantity}")
        # return "\n".join(result)

        return "\n".join(f"{product.name}: {product.quantity}" for product in self.products)




