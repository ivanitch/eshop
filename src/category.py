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

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список и увеличивает счётчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории в формате:
        'Название продукта, X руб. Остаток: X шт.'
        """
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)
