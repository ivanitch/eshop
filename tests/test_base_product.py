import pytest
from src.base_product import BaseProduct


class TestBaseProduct:

    def test_base_product_cannot_be_instantiated(self):
        """Нельзя создать объект абстрактного класса напрямую."""
        with pytest.raises(TypeError):
            BaseProduct()

    def test_product_is_instance_of_base_product(self, product_factory):
        """Product является наследником BaseProduct."""
        p = product_factory()
        assert isinstance(p, BaseProduct)

    def test_smartphone_is_instance_of_base_product(self, smartphone_factory):
        """Smartphone является наследником BaseProduct через Product."""
        s = smartphone_factory()
        assert isinstance(s, BaseProduct)

    def test_lawngrass_is_instance_of_base_product(self, lawngrass_factory):
        """LawnGrass является наследником BaseProduct через Product."""
        g = lawngrass_factory()
        assert isinstance(g, BaseProduct)
