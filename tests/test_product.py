import pytest

from src.product import Product


class TestProduct:

    def test_init_product(self, sample_product):
        assert sample_product.name == "Samsung Galaxy S23 Ultra"
        assert sample_product.description == "256GB, Серый цвет, 200MP камера"
        assert sample_product.price == 180000.0
        assert sample_product.quantity == 5

    def test_price_is_float(self, sample_product):
        assert isinstance(sample_product.price, float)

    def test_quantity_is_int(self, sample_product):
        assert isinstance(sample_product.quantity, int)

    def test_multiple_products_are_independent(self, product_factory):
        p1 = product_factory(name="A", description="desc a", price=100.0, quantity=1)
        p2 = product_factory(name="B", description="desc b", price=200.0, quantity=2)
        assert p1.name != p2.name
        assert p1.price != p2.price

    # --- __str__ ---

    def test_str_returns_string(self, sample_product):
        """__str__ возвращает строку."""
        assert isinstance(str(sample_product), str)

    def test_str_format(self, sample_product):
        """__str__ возвращает строку в формате 'Название, X руб. Остаток: X шт.'"""
        expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(sample_product) == expected

    def test_str_reflects_updated_quantity(self, sample_product):
        """__str__ отображает актуальное количество после изменения."""
        sample_product.quantity = 10
        assert "Остаток: 10 шт." in str(sample_product)

    # --- __add__ ---

    def test_add_returns_float(self, product_factory, sample_product):
        """__add__ возвращает числовое значение."""
        p2 = product_factory(name="Iphone 15", description="512GB", price=210000.0, quantity=8)
        result = sample_product + p2
        assert isinstance(result, (int, float))

    def test_add_correct_value(self, product_factory):
        """__add__ возвращает сумму произведений цены на количество."""
        a = product_factory(name="A", description="desc A", price=100.0, quantity=10)
        b = product_factory(name="B", description="desc B", price=200.0, quantity=2)
        assert a + b == 1400.0

    def test_add_is_commutative(self, product_factory):
        """Сложение коммутативно: a + b == b + a."""
        a = product_factory(name="A", description="desc A", price=100.0, quantity=10)
        b = product_factory(name="B", description="desc B", price=200.0, quantity=2)
        assert a + b == b + a

    def test_add_single_item_products(self, product_factory):
        """__add__ корректно считает, когда quantity == 1."""
        a = product_factory(name="A", description="desc A", price=100.0, quantity=1)
        b = product_factory(name="B", description="desc B", price=200.0, quantity=1)
        assert a + b == 300.0

    # --- геттер цены ---

    def test_price_getter_returns_correct_value(self, sample_product):
        assert sample_product.price == 180000.0

    def test_price_private_attribute_not_accessible(self, sample_product):
        with pytest.raises(AttributeError):
            _ = sample_product.__price  # noqa: WPS112

    # --- сеттер цены ---

    def test_price_setter_updates_valid_price(self, sample_product):
        sample_product.price = 200000.0
        assert sample_product.price == 200000.0

    def test_price_setter_rejects_zero(self, sample_product, capsys):
        sample_product.price = 0
        captured = capsys.readouterr()
        assert sample_product.price == 180000.0
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_rejects_negative(self, sample_product, capsys):
        sample_product.price = -500.0
        captured = capsys.readouterr()
        assert sample_product.price == 180000.0
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_accepts_price_on_init(self):
        p = Product("Test", "desc", 99.99, 1)
        assert p.price == 99.99

    def test_price_setter_lower_price_confirmed(self, sample_product, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "y")
        sample_product.price = 100000.0
        assert sample_product.price == 100000.0

    def test_price_setter_lower_price_rejected(self, sample_product, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "n")
        sample_product.price = 100000.0
        assert sample_product.price == 180000.0

    # --- new_product ---

    def test_new_product_returns_product_instance(self):
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 3}
        p = Product.new_product(data)
        assert isinstance(p, Product)

    def test_new_product_sets_correct_attributes(self):
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 3}
        p = Product.new_product(data)
        assert p.name == "Xiaomi 14"
        assert p.description == "256GB"
        assert p.price == 50000.0
        assert p.quantity == 3

    def test_new_product_merges_duplicate_quantities(self):
        existing = Product("Xiaomi 14", "256GB", 50000.0, 3)
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 7}
        result = Product.new_product(data, existing_products=[existing])
        assert result is existing
        assert result.quantity == 10

    def test_new_product_takes_higher_price_on_conflict(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "y")
        existing = Product("Xiaomi 14", "256GB", 50000.0, 3)
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 70000.0, "quantity": 2}
        result = Product.new_product(data, existing_products=[existing])
        assert result.price == 70000.0

    def test_new_product_no_duplicate_creates_new(self):
        existing = Product("Xiaomi 14", "256GB", 50000.0, 3)
        data = {"name": "iPhone 15", "description": "128GB", "price": 90000.0, "quantity": 1}
        result = Product.new_product(data, existing_products=[existing])
        assert result is not existing
        assert result.name == "iPhone 15"
