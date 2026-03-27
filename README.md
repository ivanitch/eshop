# EShop

Учебный проект на Python для управления каталогом товаров.

## Функциональность

- Класс `Category` — категория товаров, автоматически ведёт общий счётчик категорий и товаров через атрибуты класса
- Класс `Product` — товар с названием, описанием, ценой и количеством на складе


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
│   ├── test_сategory.py
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
```

Для отчёта о покрытии:

```bash
pytest --cov=src --cov-report=html
```

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
