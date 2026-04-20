from src.base_product import BaseEntityWithStr, BaseProduct


class Order(BaseEntityWithStr):
    """Заказ: ссылка на товар, количество и итоговая стоимость."""

    product: BaseProduct
    quantity: int
    total_cost: float

    def __init__(self, product: BaseProduct, quantity: int) -> None:
        if not isinstance(product, BaseProduct):
            raise TypeError("product должен быть наследником BaseProduct")
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, " f"количество: {self.quantity} шт., " f"итого: {self.total_cost} руб."
