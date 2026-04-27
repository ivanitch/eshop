import pytest


class TestOrder:

    def test_init_order(self, product_factory, order_factory):
        p = product_factory(price=100.0, quantity=5)
        order = order_factory(product=p, quantity=3)
        assert order.product is p
        assert order.quantity == 3
        assert order.total_cost == 300.0

    def test_total_cost_calculation(self, product_factory, order_factory):
        p = product_factory(price=500.0, quantity=10)
        order = order_factory(product=p, quantity=4)
        assert order.total_cost == 2000.0

    def test_str_format(self, product_factory, order_factory):
        p = product_factory(name="Тест", price=200.0, quantity=5)
        order = order_factory(product=p, quantity=2)
        result = str(order)
        assert "Тест" in result
        assert "400.0 руб." in result

    def test_add_invalid_product_raises_type_error(self, order_factory):
        with pytest.raises(TypeError):
            order_factory(product="не продукт", quantity=1)
