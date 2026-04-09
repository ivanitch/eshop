import pytest

from src.category import Category
from src.product import Product


class TestCategory:

    def test_init_name(self, sample_category):
        assert sample_category.name == "Смартфоны"

    def test_init_description(self, sample_category):
        assert sample_category.description == "Описание категории смартфонов"

    # --- Счётчики ---

    def test_category_count_increments(self):
        assert Category.category_count == 0
        Category("Кат1", "Описание 1", [])
        assert Category.category_count == 1
        Category("Кат2", "Описание 2", [])
        assert Category.category_count == 2

    def test_product_count_increments(self):
        p1 = Product("P1", "d", 10.0, 1)
        p2 = Product("P2", "d", 20.0, 1)
        Category("Кат1", "Описание", [p1])
        assert Category.product_count == 1
        Category("Кат2", "Описание", [p1, p2])
        assert Category.product_count == 3

    def test_category_count_accessible_via_instance(self, sample_category):
        assert sample_category.category_count == 1

    def test_product_count_accessible_via_instance(self, sample_category):
        assert sample_category.product_count == 2

    def test_empty_category_does_not_add_products(self):
        Category("Пустая", "Описание", [])
        assert Category.product_count == 0

    def test_counters_are_shared_across_instances(self):
        Category("А", "d", [Product("X", "d", 1.0, 1)])
        Category("Б", "d", [Product("Y", "d", 2.0, 1), Product("Z", "d", 3.0, 1)])
        assert Category.category_count == 2
        assert Category.product_count == 3

    # --- __str__ ---

    def test_str_returns_string(self, sample_category):
        """__str__ возвращает строку."""
        assert isinstance(str(sample_category), str)

    def test_str_contains_category_name(self, sample_category):
        """__str__ содержит название категории."""
        assert "Смартфоны" in str(sample_category)

    def test_str_contains_total_quantity(self, sample_category):
        """__str__ считает суммарное количество (5 + 8 = 13)."""
        assert "13 шт." in str(sample_category)

    def test_str_format(self, sample_category):
        """__str__ возвращает строку в формате 'Название категории, количество продуктов: X шт.'"""
        assert str(sample_category) == "Смартфоны, количество продуктов: 13 шт."

    def test_str_empty_category(self):
        """__str__ для пустой категории возвращает 0 шт."""
        cat = Category("Пустая", "Описание", [])
        assert str(cat) == "Пустая, количество продуктов: 0 шт."

    def test_str_updates_after_add_product(self, sample_category):
        """__str__ отражает актуальное количество после add_product."""
        new_product = Product("Pixel 8", "128GB", 75000.0, 3)
        sample_category.add_product(new_product)
        assert "16 шт." in str(sample_category)

    # --- add_product ---

    def test_add_product_increases_product_count(self, sample_category):
        before = Category.product_count
        new_product = Product("Pixel 8", "128GB, Obsidian", 75000.0, 3)
        sample_category.add_product(new_product)
        assert Category.product_count == before + 1

    def test_add_product_appears_in_products_string(self, sample_category):
        new_product = Product("Pixel 8", "128GB, Obsidian", 75000.0, 3)
        sample_category.add_product(new_product)
        assert "Pixel 8" in sample_category.products

    def test_add_product_accepts_product_instance(self):
        cat = Category("Тест", "Описание", [])
        product = Product("OnePlus 12", "256GB", 60000.0, 10)
        cat.add_product(product)
        assert Category.product_count == 1

    # --- products property ---

    def test_products_returns_string(self, sample_category):
        assert isinstance(sample_category.products, str)

    def test_products_contains_both_product_names(self, sample_category):
        products_str = sample_category.products
        assert "Samsung Galaxy S23 Ultra" in products_str
        assert "Iphone 15" in products_str

    def test_products_format(self, sample_category):
        products_str = sample_category.products
        assert "180000.0 руб. Остаток: 5 шт." in products_str
        assert "210000.0 руб. Остаток: 8 шт." in products_str

    def test_products_not_directly_accessible(self, sample_category):
        with pytest.raises(AttributeError):
            _ = sample_category.__products  # noqa: WPS112

    def test_empty_category_products_is_empty_string(self):
        cat = Category("Пустая", "Описание", [])
        assert cat.products == ""
