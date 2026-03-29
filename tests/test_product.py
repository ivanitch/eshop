import pytest

from src.product import Product


class TestProduct:

    def test_init_name(self, sample_product):
        assert sample_product.name == "Samsung Galaxy S23 Ultra"

    def test_init_description(self, sample_product):
        assert sample_product.description == "256GB, Серый цвет, 200MP камера"

    def test_init_price(self, sample_product):
        assert sample_product.price == 180000.0

    def test_init_quantity(self, sample_product):
        assert sample_product.quantity == 5

    def test_price_is_float(self, sample_product):
        assert isinstance(sample_product.price, float)

    def test_quantity_is_int(self, sample_product):
        assert isinstance(sample_product.quantity, int)

    def test_multiple_products_are_independent(self):
        p1 = Product("A", "desc a", 100.0, 1)
        p2 = Product("B", "desc b", 200.0, 2)
        assert p1.name != p2.name
        assert p1.price != p2.price

    # --- геттер цены ---

    def test_price_getter_returns_correct_value(self, sample_product):
        """Геттер price возвращает значение приватного атрибута."""
        assert sample_product.price == 180000.0

    def test_price_private_attribute_not_accessible(self, sample_product):
        """Приватный атрибут __price недоступен напрямую снаружи."""
        with pytest.raises(AttributeError):
            _ = sample_product.__price  # noqa: WPS112

    # --- сеттер цены ---

    def test_price_setter_updates_valid_price(self, sample_product):
        """Сеттер принимает положительную цену и обновляет атрибут."""
        sample_product.price = 200000.0
        assert sample_product.price == 200000.0

    def test_price_setter_rejects_zero(self, sample_product, capsys):
        """Сеттер не обновляет цену при значении 0 и выводит сообщение."""
        sample_product.price = 0
        captured = capsys.readouterr()
        assert sample_product.price == 180000.0
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_rejects_negative(self, sample_product, capsys):
        """Сеттер не обновляет цену при отрицательном значении и выводит сообщение."""
        sample_product.price = -500.0
        captured = capsys.readouterr()
        assert sample_product.price == 180000.0
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_accepts_price_on_init(self):
        """Цена корректно устанавливается через сеттер при создании объекта."""
        p = Product("Test", "desc", 99.99, 1)
        assert p.price == 99.99

    # --- подтверждение снижения цены ---

    def test_price_setter_lower_price_confirmed(self, sample_product, monkeypatch):
        """При снижении цены и подтверждении 'y' цена обновляется."""
        monkeypatch.setattr("builtins.input", lambda _: "y")
        sample_product.price = 100000.0
        assert sample_product.price == 100000.0

    def test_price_setter_lower_price_rejected(self, sample_product, monkeypatch):
        """При снижении цены и отказе ('n') цена остаётся прежней."""
        monkeypatch.setattr("builtins.input", lambda _: "n")
        sample_product.price = 100000.0
        assert sample_product.price == 180000.0

    # --- new_product ---

    def test_new_product_returns_product_instance(self):
        """new_product() возвращает объект класса Product."""
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 3}
        p = Product.new_product(data)
        assert isinstance(p, Product)

    def test_new_product_sets_correct_attributes(self):
        """new_product() корректно устанавливает все атрибуты товара."""
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 3}
        p = Product.new_product(data)
        assert p.name == "Xiaomi 14"
        assert p.description == "256GB"
        assert p.price == 50000.0
        assert p.quantity == 3

    # --- дедупликация через new_product ---

    def test_new_product_merges_duplicate_quantities(self):
        """Если товар с таким именем уже есть, количества суммируются."""
        existing = Product("Xiaomi 14", "256GB", 50000.0, 3)
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 7}
        result = Product.new_product(data, existing_products=[existing])
        assert result is existing
        assert result.quantity == 10

    def test_new_product_takes_higher_price_on_conflict(self, monkeypatch):
        """При конфликте цен выбирается более высокая цена."""
        monkeypatch.setattr("builtins.input", lambda _: "y")
        existing = Product("Xiaomi 14", "256GB", 50000.0, 3)
        data = {"name": "Xiaomi 14", "description": "256GB", "price": 70000.0, "quantity": 2}
        result = Product.new_product(data, existing_products=[existing])
        assert result.price == 70000.0

    def test_new_product_no_duplicate_creates_new(self):
        """Если товара с таким именем нет, создаётся новый объект."""
        existing = Product("Xiaomi 14", "256GB", 50000.0, 3)
        data = {"name": "iPhone 15", "description": "128GB", "price": 90000.0, "quantity": 1}
        result = Product.new_product(data, existing_products=[existing])
        assert result is not existing
        assert result.name == "iPhone 15"
