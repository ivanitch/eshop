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
- Класс `ZeroQuantityError` — пользовательское исключение, вызываемое при попытке добавить товар с нулевым количеством

## Реализованные возможности

### Category

- Приватный атрибут `__products` для хранения списка товаров
- Метод `add_product(product)` — добавляет товар в категорию и увеличивает `product_count`.
  Принимает только экземпляры `Product` или его наследников; при передаче любого другого объекта выбрасывает `TypeError`.
  При добавлении товара с нулевым количеством вызывает `ZeroQuantityError` и выводит сообщение об ошибке.
  В любом случае выводит сообщение о завершении обработки (`finally`).
  При успешном добавлении выводит подтверждение (`else`).
- Свойство `products` (геттер) — возвращает строку со всеми товарами в формате:
  `Название продукта, X руб. Остаток: X шт.`
- Метод `middle_price()` — возвращает средний ценник всех товаров категории.
  При пустой категории (деление на ноль) возвращает `0`.
- Метод `__str__` — возвращает строку в формате:
  `Название категории, количество продуктов: X шт.`
  где X — суммарное количество всех товаров на складе

### Product

- При создании товара с `quantity == 0` выбрасывается `ValueError` с сообщением
  «Товар с нулевым количеством не может быть добавлен»
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
│   ├── exceptions.py      # пользовательские исключения (ZeroQuantityError)
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
src/category.py          30      0   100%
src/exceptions.py         3      0   100%
src/lawngrass.py          8      0   100%
src/mixins.py             6      0   100%
src/order.py             13      0   100%
src/product.py           51      0   100%
src/smartphone.py        10      0   100%
-----------------------------------------
TOTAL                   133      3    98%

```

---

## Пример использования

```python
from src.category import Category
from src.product import Product


if __name__ == '__main__':
    try:
        product_invalid = Product(
            "Бракованный товар",
            "Неверное количество",
            1000.0,
            "green",
            0
        )
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        "Серый",
        5
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        "Gray",
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        "Синий",
        14
    )

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
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
