# EShop

Учебный проект по созданию системы управления каталогом товаров на Python, разработанный в рамках курса
«Python-разработчик с нуля» от онлайн-университета Skypro.

## Функциональность

- Класс `Category` — категория товаров, автоматически ведёт общий счётчик категорий и товаров через атрибуты класса
- Класс `Product` — товар с названием, описанием, ценой, цветом и количеством на складе
- Класс `Smartphone` — наследник `Product`, расширен атрибутами: производительность, модель, объём памяти
- Класс `LawnGrass` — наследник `Product`, расширен атрибутами: страна-производитель, срок прорастания
- Класс `BaseProduct` — абстрактный базовый класс, задаёт интерфейс для всех продуктов (обязательные методы `__str__` и `__add__`)
- Класс `LogMixin` — миксин, который при создании любого объекта-продукта автоматически выводит в консоль его класс и параметры
- Класс `Order` — заказ, содержит ссылку на товар, количество и итоговую стоимость

## Реализованные возможности

### Category

- Приватный атрибут `__products` для хранения списка товаров
- Метод `add_product(product)` — добавляет товар в категорию и увеличивает `product_count`.
  Принимает только экземпляры `Product` или его наследников; при передаче любого другого объекта выбрасывает `TypeError`
- Свойство `products` (геттер) — возвращает строку со всеми товарами в формате:
  `Название продукта, X руб. Остаток: X шт.`
- Метод `__str__` — возвращает строку в формате:
  `Название категории, количество продуктов: X шт.`
  где X — суммарное количество всех товаров на складе

### Product

- Приватный атрибут `__price` с геттером и сеттером через `@property`
- Сеттер цены проверяет значение: при цене ≤ 0 выводит сообщение и не обновляет цену
- При снижении цены запрашивает подтверждение у пользователя (`y` — принять, любой другой — отменить)
- Класс-метод `new_product(product_dict, existing_products=None)` — создаёт `Product` из словаря;
  при совпадении имени с существующим товаром суммирует количества и берёт максимальную цену
- Метод `__str__` — возвращает строку в формате:
  `Название продукта, X руб. Остаток: X шт.`
- Метод `__add__` — возвращает полную стоимость двух товаров на складе:
  `цена_1 × количество_1 + цена_2 × количество_2`.
  Складывать можно только товары **одного и того же класса**; при попытке сложить объекты разных классов
  выбрасывается `TypeError`

### Smartphone

Наследник `Product`. Дополнительные атрибуты:

- `efficiency` — производительность
- `model` — модель
- `memory` — объём встроенной памяти

### LawnGrass

Наследник `Product`. Дополнительные атрибуты:

- `country` — страна-производитель
- `germination_period` — срок прорастания

## Структура проекта

```
.
├── src/
│   ├── __init__.py
│   ├── base_product.py    # абстрактный базовый класс BaseProduct и BaseEntityWithStr
│   ├── category.py        # класс категории товаров
│   ├── lawngrass.py       # класс газонной травы (наследник Product)
│   ├── mixins.py          # класс-миксин LogMixin
│   ├── order.py           # класс заказа Order
│   ├── product.py         # базовый класс товара
│   └── smartphone.py      # класс смартфона (наследник Product)
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_base_product.py
│   ├── test_category.py
│   ├── test_lawngrass.py
│   ├── test_mixins.py
│   ├── test_order.py
│   ├── test_product.py
│   └── test_smartphone.py
│
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

poetry run python main.py
```

## Запуск тестов

```bash
poetry run pytest

# Подробный вывод
poetry run pytest -v

# С отчётом о покрытии кода
poetry run pytest tests -v --cov=src --cov-report=html
```

### Просмотр покрытия

```bash
poetry run coverage report                 # таблица в консоли

poetry run coverage report > coverage.txt  # направить отчёт в файл `coverage.txt`

poetry run coverage html                   # HTML-отчёт в папке htmlcov/ с интерактивным сайтом (htmlcov/index.html)
```

Файл `coverage.txt`:

```
Name                  Stmts   Miss  Cover
-----------------------------------------
src/__init__.py           0      0   100%
src/base_product.py      12      3    75%
src/category.py          25      0   100%
src/lawngrass.py          8      0   100%
src/mixins.py             6      0   100%
src/order.py             13      0   100%
src/product.py           49      0   100%
src/smartphone.py        10      0   100%
-----------------------------------------
TOTAL                   123      3    98%

```

---

## Пример использования

```python
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass

smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB", 180000.0, "Серый", 5, "High", "S23 Ultra", 256)
smartphone2 = Smartphone("Iphone 15", "512GB", 210000.0, "Gray space", 8, "High", "15", 512)

# __str__ для Smartphone
print(str(smartphone1))
# Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.

# __add__ — только одинаковые классы
print(smartphone1 + smartphone2)
# 2580000.0  (180000 × 5 + 210000 × 8)

grass = LawnGrass("Газонная трава", "Элитная", 500.0, "Зеленый", 20, "Россия", "7 дней")

# Сложение разных типов — ошибка
try:
    result = smartphone1 + grass
except TypeError as e:
    print(e)  # Нельзя складывать продукты разных типов: Smartphone и LawnGrass

category = Category("Смартфоны", "Описание", [smartphone1, smartphone2])

# __str__ для Category — суммарное количество товаров
print(str(category))
# Смартфоны, количество продуктов: 13 шт.

# add_product — только Product и наследники
category.add_product(smartphone2)  # OK

try:
    category.add_product("не продукт")
except TypeError as e:
    print(e)  # Можно добавлять только объекты класса Product и его наследников
```

## Кодстайл

```bash
poetry run flake8 src tests          # линтер
poetry run black src tests           # форматирование
poetry run isort src tests           # сортировка импортов
poetry run mypy src                  # проверка типов
```

Или запустить все линтеры одной командой:

```bash
poetry run ./lint.sh
```
