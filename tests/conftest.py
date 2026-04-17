import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сбрасывает счётчики класса перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def sample_product(product_factory):
    return product_factory()


@pytest.fixture
def sample_category(product_factory, category_factory):
    product_1 = product_factory()
    product_2 = product_factory(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)
    return category_factory(products=[product_1, product_2])


@pytest.fixture
def product_factory():
    """Фабрика для создания продуктов с дефолтными значениями"""

    def _make_product(**kwargs):
        params = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
        params.update(kwargs)
        return Product(**params)

    return _make_product


@pytest.fixture
def category_factory(product_factory):
    def _make_category(**kwargs):
        # Если продукты не переданы, создаем один по умолчанию
        if "products" not in kwargs:
            kwargs["products"] = [product_factory()]

        params = {
            "name": "Смартфоны",
            "description": "Описание категории",
        }
        params.update(kwargs)
        return Category(**params)

    return _make_category
