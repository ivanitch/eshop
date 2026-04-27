import pytest

from src.category import Category


class TestCategory:

    def test_init_category(self, sample_category):
        assert sample_category.name == "Смартфоны"
        assert sample_category.description == "Описание категории"

    def test_category_count_increments(self, category_factory):
        assert Category.category_count == 0
        category_factory(name="Кат1", description="Описание 1", products=[])
        assert Category.category_count == 1
        category_factory(name="Кат2", description="Описание 2", products=[])
        assert Category.category_count == 2

    def test_product_count_increments(self, product_factory, category_factory):
        p1 = product_factory(name='P1', description='d', price=10.0, quantity=1)
        p2 = product_factory(name='P2', description='d', price=20.0, quantity=1)
        category_factory(name='Кат1', description='Описание', products=[p1])
        assert Category.product_count == 1
        category_factory(name='Кат2', description='Описание', products=[p1, p2])
        assert Category.product_count == 3

    def test_category_count_accessible_via_instance(self, sample_category):
        assert sample_category.category_count == 1

    def test_product_count_accessible_via_instance(self, sample_category):
        assert sample_category.product_count == 2

    def test_empty_category_does_not_add_products(self, category_factory):
        category_factory(name="Пустая", description="Описание", products=[])
        assert Category.product_count == 0

    def test_counters_are_shared_across_instances(self, category_factory, product_factory):
        category_factory(
            name="А",
            description="d",
            products=[product_factory(name='X', description='d', price=1.0, quantity=1)]
        )

        category_factory(
            name="B",
            description="d",
            products=[
                product_factory(name='Y', description='d', price=2.0, quantity=1),
                product_factory(name='Z', description='d', price=3.0, quantity=1)
            ]
        )

        assert Category.category_count == 2
        assert Category.product_count == 3

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

    def test_str_empty_category(self, category_factory):
        """__str__ для пустой категории возвращает 0 шт."""
        cat = category_factory(name="Пустая", description="Описание", products=[])
        assert str(cat) == "Пустая, количество продуктов: 0 шт."

    def test_str_updates_after_add_product(self, sample_category, product_factory):
        """__str__ отражает актуальное количество после add_product."""
        new_product = product_factory(name="Pixel 8", description="128GB", price=75000.0, quantity=3)
        sample_category.add_product(new_product)
        assert "16 шт." in str(sample_category)

    def test_add_product_increases_product_count(self, sample_category, product_factory):
        before = Category.product_count
        new_product = product_factory(name="Pixel 8", description="128GB, Obsidian", price=75000.0, quantity=3)
        sample_category.add_product(new_product)
        assert Category.product_count == before + 1

    def test_add_product_appears_in_products_string(self, sample_category, product_factory):
        new_product = product_factory(name="Pixel 8", description="128GB, Obsidian", price=75000.0, quantity=3)
        sample_category.add_product(new_product)
        assert "Pixel 8" in sample_category.products

    def test_add_product_accepts_product_instance(self, category_factory, product_factory):
        cat = category_factory(name="Тест", description="Описание", products=[])
        product = product_factory(name="OnePlus 12", description="256GB", price=60000.0, quantity=10)
        cat.add_product(product)
        assert Category.product_count == 1

    def test_add_product_accepts_smartphone(self, category_factory, smartphone_factory):
        """add_product принимает объект Smartphone как наследника Product."""
        cat = category_factory(name="Смартфоны", description="Описание", products=[])
        smartphone = smartphone_factory()
        cat.add_product(smartphone)
        assert Category.product_count == 1

    def test_add_product_accepts_lawngrass(self, category_factory, lawngrass_factory):
        """add_product принимает объект LawnGrass как наследника Product."""
        cat = category_factory(name="Трава", description="Описание", products=[])
        grass = lawngrass_factory()
        cat.add_product(grass)
        assert Category.product_count == 1

    def test_add_product_rejects_string(self, category_factory):
        """add_product выбрасывает TypeError при передаче строки."""
        cat = category_factory(name="Тест", description="Описание", products=[])
        with pytest.raises(TypeError):
            cat.add_product("не продукт")

    def test_add_product_rejects_int(self, category_factory):
        """add_product выбрасывает TypeError при передаче числа."""
        cat = category_factory(name="Тест", description="Описание", products=[])
        with pytest.raises(TypeError):
            cat.add_product(42)

    def test_add_product_rejects_dict(self, category_factory):
        """add_product выбрасывает TypeError при передаче словаря."""
        cat = category_factory(name="Тест", description="Описание", products=[])
        with pytest.raises(TypeError):
            cat.add_product({"name": "Продукт"})

    def test_add_product_rejects_none(self, category_factory):
        """add_product выбрасывает TypeError при передаче None."""
        cat = category_factory(name="Тест", description="Описание", products=[])
        with pytest.raises(TypeError):
            cat.add_product(None)

    def test_add_product_does_not_increase_count_on_error(self, category_factory):
        """При ошибке product_count не увеличивается."""
        cat = category_factory(name="Тест", description="Описание", products=[])
        before = Category.product_count
        with pytest.raises(TypeError):
            cat.add_product("не продукт")
        assert Category.product_count == before

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

    def test_empty_category_products_is_empty_string(self, category_factory):
        cat = category_factory(name="Пустая", description="Описание", products=[])
        assert cat.products == ""

    def test_middle_price_returns_float(self, sample_category):
        """middle_price возвращает числовое значение."""
        result = sample_category.middle_price()
        assert isinstance(result, (int, float))

    def test_middle_price_correct_value(self, product_factory, category_factory):
        """middle_price возвращает среднее арифметическое цен (только цены, не quantity)."""
        p1 = product_factory(name="A", description="d", price=100.0, quantity=1)
        p2 = product_factory(name="B", description="d", price=200.0, quantity=1)
        p3 = product_factory(name="C", description="d", price=300.0, quantity=1)
        cat = category_factory(name="Тест", description="d", products=[p1, p2, p3])
        assert cat.middle_price() == 200.0

    def test_middle_price_single_product(self, product_factory, category_factory):
        """middle_price для одного товара равна его цене."""
        p = product_factory(name="A", description="d", price=500.0, quantity=10)
        cat = category_factory(name="Тест", description="d", products=[p])
        assert cat.middle_price() == 500.0

    def test_middle_price_empty_category_returns_zero(self, category_factory):
        """middle_price возвращает 0 для пустой категории."""
        cat = category_factory(name="Пустая", description="Описание", products=[])
        assert cat.middle_price() == 0

    def test_middle_price_ignores_quantity(self, product_factory, category_factory):
        """middle_price учитывает только self.price, не умножает на quantity."""
        p1 = product_factory(name="A", description="d", price=1000.0, quantity=100)
        p2 = product_factory(name="B", description="d", price=2000.0, quantity=1)
        cat = category_factory(name="Тест", description="d", products=[p1, p2])
        assert cat.middle_price() == 1500.0
