import pytest
from products import Product  # Import your Product class


def test_product_initialization():
    p = Product("Laptop", price=1200.50, quantity=10)
    assert p.name == "Laptop"
    assert p.price == 1200.50
    assert p.quantity == 10
    assert p.is_active is True


def test_invalid_initialization():
    with pytest.raises(Exception):
        Product("", price=1200.50, quantity=10)  # Empty name
    with pytest.raises(Exception):
        Product("Laptop", price=-50.0, quantity=10)  # Negative price
    with pytest.raises(Exception):
        Product("Laptop", price=1200.50, quantity=-5)  # Negative quantity


def test_get_quantity():
    p = Product("Phone", price=800.0, quantity=5)
    assert p.get_quantity() == 5


def test_set_quantity():
    p = Product("Tablet", price=300.0, quantity=5)
    p.set_quantity(5)
    assert p.get_quantity() == 10

    p.set_quantity(-10)  # Should set quantity to 0
    assert p.get_quantity() == 0
    assert p.get_status() is False  # Product should be inactive


def test_buy():
    p = Product("Monitor", price=200.0, quantity=10)
    assert p.buy(2) == 400.0
    assert p.get_quantity() == 8

    with pytest.raises(Exception):
        p.buy(20)  # Not enough stock

    with pytest.raises(Exception):
        p.buy(-1)  # Invalid quantity


def test_status():
    p = Product("Keyboard", price=50.0, quantity=1)
    assert p.get_status() is True  # Initially active

    p.buy(1)  # Reduce quantity to 0
    assert p.get_status() is False  # Should now be inactive


def test_activation():
    p = Product("Mouse", price=30.0, quantity=10)
    p.deactivate()
    assert p.get_status() is False

    p.activate()
    assert p.get_status() is True
