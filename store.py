from products import Product


class Store:
    def __init__(self, product_list):
        if not isinstance(product_list, list) or not product_list:
            raise Exception("product_list must be a non-empty list!")
        self.product_list = product_list

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise Exception("Only instances of Product can be added!")
        self.product_list.append(product)

    def remove_product(self, product: Product):
        if product in self.product_list:
            self.product_list.remove(product)
        else:
            raise Exception("Product not found in store!")

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self):
        return [product.show() for product in self.product_list if product.get_status()]


    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

