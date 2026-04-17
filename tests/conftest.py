import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


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
def sample_smartphone(smartphone_factory):
    return smartphone_factory()


@pytest.fixture
def sample_lawngrass(lawngrass_factory):
    return lawngrass_factory()


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
            "color": 'white',
            "quantity": 5,
        }
        params.update(kwargs)
        return Product(**params)

    return _make_product


@pytest.fixture
def smartphone_factory():
    """Фабрика для создания смартфонов"""

    def _make_smartphone(**kwargs):
        params = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
            "efficiency": "High",
            "model": "S23 Ultra",
            "memory": 256,
            "color": "Grey"
        }
        params.update(kwargs)
        return Smartphone(**params)

    return _make_smartphone


@pytest.fixture
def lawngrass_factory():
    """Фабрика для создания 'Трава газонная'"""

    def _make_lawngrass(**kwargs):
        params = {
            "name": "Газонная трава",
            "description": "Элитная трава для газона",
            "price": 500.0,
            "color": "Зеленый",
            "quantity": 20,
            "country": "Россия",
            "germination_period": "7 дней"
        }
        params.update(kwargs)
        return LawnGrass(**params)

    return _make_lawngrass


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
