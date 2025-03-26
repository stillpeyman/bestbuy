class Product:
    def __init__(self, name, price, quantity, is_active=True):
        if not isinstance(name, str) or not name:
            raise Exception("Error, name must be a non-empty string!")

        if not isinstance(price, (int, float)) or price <= 0:
            raise Exception("Error, price must be float and greater than 0!")

        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Error, quantity must be integer and greater or equal to 0!")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.is_active = is_active

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity == 0:
            self.is_active = False

    def get_status(self):
        return self.is_active

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Error, quantity must be integer and greater than 0!")

        if quantity > self.quantity:
            raise Exception("Error, insufficient quantity!")

        if not self.is_active:
            raise Exception("Error, product is out of stock!")

        self.quantity -= quantity

        if self.quantity == 0:
            self.is_active = False

        return self.price * quantity
