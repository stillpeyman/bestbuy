class Product:

    def __init__(self, name, price, quantity, is_active=True):
        """
        Get product name, price and quantity and initializes
        a product, by default is_active (availability) set to 'True'.
        """
        if not isinstance(name, str) or not name:
            raise Exception("Error, name must be a non-empty string!")

        if not isinstance(price, (int, float)) or price <= 0:
            raise Exception("Error, price must be float and greater than 0!")

        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Error, quantity must be a positive integer!")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.is_active = is_active


    def get_quantity(self):
        """
        Getter function for quantity.
        Return the quantity (int).
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise Exception("Error, quantity must be a positive integer!")

        self.quantity = quantity

        if self.quantity == 0:
            self.is_active = False


    def get_status(self):
        """
        Getter function for active.
        Return True if the product is active, otherwise False.
        """
        return self.is_active


    def activate(self):
        """
        Activate the product.
        """
        self.is_active = True


    def deactivate(self):
        """
        Deactivate the product.
        """
        self.is_active = False


    def show(self):
        """
        Return a string that represents the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        Buy a given quantity of the product.
        Return total price (float) of the purchase.
        Update the quantity of the product.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Error, quantity must be integer and greater than 0!")

        if quantity > self.quantity:
            raise Exception("Error, insufficient quantity!")

        if not self.is_active:
            raise Exception("Error, product is out of stock!")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity


    def calculate_price(self, quantity):
        """
        Calculate total price for a given quantity, applying promotions if available,
        without actually buying the product or modifying its quantity.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise Exception("Error, quantity must be integer and greater than 0!")

        if not self.is_active:
            raise Exception("Error, product is unavailable at the moment!")

        return self.price * quantity
