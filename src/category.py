from src.base_product import BaseEntityWithStr
from src.product import Product


class Category(BaseEntityWithStr):
    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список и увеличивает счётчик товаров.

        Принимает только объекты класса Product и его наследников.
        Raises:
            TypeError: если переданный объект не является экземпляром Product.
        """
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты класса Product и его наследников, "
                f"получен: {type(product).__name__}"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории в формате:
        'Название продукта, X руб. Остаток: X шт.'
        """
        return "\n".join(str(product) for product in self.__products)
