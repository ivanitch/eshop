from src.product import Product


class Smartphone(Product):
    efficiency: str
    model: str
    memory: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        color: str,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
    ) -> None:
        super().__init__(name, description, price, color, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
