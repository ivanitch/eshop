from src.product import Product


class Category:
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
        """Добавляет продукт в приватный список и увеличивает счётчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории в формате:
        'Название продукта, X руб. Остаток: X шт.'
        """
        return "\n".join(str(product) for product in self.__products)
