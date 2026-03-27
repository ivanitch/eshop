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
def sample_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def sample_category(sample_product):
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Смартфоны", "Описание категории смартфонов", [sample_product, product_2])
