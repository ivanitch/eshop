import pytest


class TestSmartphone:

    def test_init_smartphone(self, sample_smartphone):
        assert sample_smartphone.name == "Samsung Galaxy S23 Ultra"
        assert sample_smartphone.description == "256GB, Серый цвет, 200MP камера"
        assert sample_smartphone.price == 180000.0
        assert sample_smartphone.color == "Grey"
        assert sample_smartphone.quantity == 5
        assert sample_smartphone.efficiency == "High"
        assert sample_smartphone.memory == 256

    def test_smartphone_is_product_subclass(self, sample_smartphone):
        """Smartphone является наследником Product."""
        from src.product import Product
        assert isinstance(sample_smartphone, Product)

    def test_str_format(self, sample_smartphone):
        """__str__ возвращает строку в формате 'Название, X руб. Остаток: X шт.'"""
        expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(sample_smartphone) == expected

    def test_add_two_smartphones(self, smartphone_factory):
        """Два смартфона складываются без ошибок."""
        s1 = smartphone_factory(price=180000.0, quantity=5)
        s2 = smartphone_factory(name="Iphone 15", price=210000.0, quantity=8)
        result = s1 + s2
        assert result == 180000.0 * 5 + 210000.0 * 8

    def test_add_smartphone_and_lawngrass_raises_type_error(self, smartphone_factory, lawngrass_factory):
        """Сложение Smartphone и LawnGrass выбрасывает TypeError."""
        smartphone = smartphone_factory()
        grass = lawngrass_factory()
        with pytest.raises(TypeError):
            _ = smartphone + grass
