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
