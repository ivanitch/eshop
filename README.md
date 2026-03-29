# EShop

Учебный проект по созданию системы управления каталогом товаров на Python, разработанный в рамках курса «Python-разработчик с нуля» от онлайн-университета Skypro.

## Функциональность

- Класс `Category` — категория товаров, автоматически ведёт общий счётчик категорий и товаров через атрибуты класса
- Класс `Product` — товар с названием, описанием, ценой и количеством на складе

## Реализованные возможности

### Category
- Приватный атрибут `__products` для хранения списка товаров
- Метод `add_product(product)` — добавляет товар в категорию и увеличивает `product_count`
- Свойство `products` (геттер) — возвращает строку со всеми товарами в формате:
  `Название продукта, X руб. Остаток: X шт.`

### Product
- Приватный атрибут `__price` с геттером и сеттером через `@property`
- Сеттер цены проверяет значение: при цене ≤ 0 выводит сообщение и не обновляет цену
- При снижении цены запрашивает подтверждение у пользователя (`y` — принять, любой другой — отменить)
- Класс-метод `new_product(product_dict, existing_products=None)` — создаёт `Product` из словаря;
  при совпадении имени с существующим товаром суммирует количества и берёт максимальную цену

## Структура проекта

```
.
├── src/
│   ├── __init__.py
│   ├── category.py        # класс категории товаров
│   └── product.py         # класс товара
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_category.py
│   └── test_product.py
├── .flake8
├── .gitignore
├── lint.sh
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Установка и запуск

Клонируйте репозиторий и установите зависимости через poetry:

```bash
git clone git@github.com:ivanitch/eshop.git
cd eshop
poetry install
```

## Запуск тестов

```bash
pytest

# Подробный вывод
pytest -v

# С отчётом о покрытии кода
pytest tests -v --cov=src --cov-report=html
```

### Просмотр покрытия

```bash
coverage report          # таблица в консоли
coverage html            # HTML-отчёт в папке `htmlcov/` с интерактивным сайтом. Открыть: `path/to/project/htmlcov/index.html`
```

---


## Пример использования

```python
from src.category import Category
from src.product import Product

# Создание объектов вручную
product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
category = Category("Смартфоны", "Описание", [product])

print(category.name)            # Смартфоны
print(Category.category_count)  # 1
print(Category.product_count)   # 1

# Добавление товара через метод
new_product = Product("Pixel 8", "128GB", 75000.0, 3)
category.add_product(new_product)
print(category.products)
# Iphone 15, 210000.0 руб. Остаток: 8 шт.
# Pixel 8, 75000.0 руб. Остаток: 3 шт.

# Создание товара из словаря
p = Product.new_product({"name": "Xiaomi 14", "description": "256GB", "price": 50000.0, "quantity": 5})

# Сеттер с валидацией цены
p.price = -100   # Цена не должна быть нулевая или отрицательная
p.price = 60000  # ОК (повышение)
p.price = 40000  # Запрос подтверждения (снижение)
```

## Кодстайл

```bash
flake8 src tests          # линтер
black src tests           # форматирование
isort src tests           # сортировка импортов
mypy src                  # проверка типов
```

Или запустить все линтеры одной командой:

```bash
./lint.sh
```
