from src.mixins import LogMixin


class TestLogMixin:

    def test_product_inherits_log_mixin(self, product_factory):
        """Product является наследником LogMixin."""
        p = product_factory()
        assert isinstance(p, LogMixin)

    def test_log_mixin_prints_on_creation(self, product_factory, capsys):
        """При создании объекта LogMixin печатает информацию в консоль."""
        product_factory(name="Test", description="Desc", price=100.0, quantity=1)
        captured = capsys.readouterr()
        assert "Test" in captured.out

    def test_repr_contains_class_name(self, product_factory):
        """__repr__ содержит имя класса."""
        p = product_factory()
        assert "Product" in repr(p)

    def test_repr_contains_name(self, product_factory):
        p = product_factory(name="MyProduct", description="d", price=10.0, quantity=1)
        assert "MyProduct" in repr(p)

    def test_smartphone_repr_contains_smartphone(self, smartphone_factory, capsys):
        """При создании Smartphone repr показывает 'Smartphone', а не 'Product'."""
        s = smartphone_factory()
        assert "Smartphone" in repr(s)
