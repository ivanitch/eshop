from src.product import Product


class LawnGrass(Product):
    country: str
    germination_period: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        color: str,
        quantity: int,
        country: str,
        germination_period: str,
    ) -> None:
        super().__init__(name, description, price, color, quantity)
        self.country = country
        self.germination_period = germination_period
