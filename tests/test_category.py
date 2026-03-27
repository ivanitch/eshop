from src.category import Category
from src.product import Product


class TestCategory:
    def test_init_name(self, sample_category):
        assert sample_category.name == "Смартфоны"

    def test_init_description(self, sample_category):
        assert sample_category.description == "Описание категории смартфонов"

    def test_init_products_length(self, sample_category):
        assert len(sample_category.products) == 2

    def test_products_are_product_instances(self, sample_category):
        for product in sample_category.products:
            assert isinstance(product, Product)

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
