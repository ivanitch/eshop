import pytest


class TestLawnGrass:

    def test_init_lawngrass(self, sample_lawngrass):
        assert sample_lawngrass.name == "Газонная трава"
        assert sample_lawngrass.description == "Элитная трава для газона"
        assert sample_lawngrass.price == 500.0
        assert sample_lawngrass.color == "Зеленый"
        assert sample_lawngrass.quantity == 20
        assert sample_lawngrass.country == "Россия"
        assert sample_lawngrass.germination_period == '7 дней'

    def test_lawngrass_is_product_subclass(self, sample_lawngrass):
        """LawnGrass является наследником Product."""
        from src.product import Product
        assert isinstance(sample_lawngrass, Product)

    def test_str_format(self, sample_lawngrass):
        """__str__ возвращает строку в формате 'Название, X руб. Остаток: X шт.'"""
        expected = "Газонная трава, 500.0 руб. Остаток: 20 шт."
        assert str(sample_lawngrass) == expected

    def test_add_two_lawngrasses(self, lawngrass_factory):
        """Две газонные травы складываются без ошибок."""
        g1 = lawngrass_factory(price=500.0, quantity=20)
        g2 = lawngrass_factory(name="Газонная трава 2", price=450.0, quantity=15)
        result = g1 + g2
        assert result == 500.0 * 20 + 450.0 * 15

    def test_add_lawngrass_and_smartphone_raises_type_error(self, lawngrass_factory, smartphone_factory):
        """Сложение LawnGrass и Smartphone выбрасывает TypeError."""
        grass = lawngrass_factory()
        smartphone = smartphone_factory()
        with pytest.raises(TypeError):
            _ = grass + smartphone
