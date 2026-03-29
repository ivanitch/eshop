class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price  # через сеттер
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if hasattr(self, "_Product__price") and value < self.__price:
            answer = input(
                f'Цена товара "{self.name}" понижается с {self.__price} до {value}. ' f"Подтвердите действие (y/n): "
            )
            if answer != "y":
                return
        self.__price = value

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list | None = None) -> "Product":
        """Создаёт и возвращает объект Product из словаря с параметрами товара.

        Доп. задание 3: если передан список existing_products и товар с таким же
        именем уже есть — суммирует количество и выбирает максимальную цену.
        """
        name = product_dict["name"]
        description = product_dict["description"]
        price = float(product_dict["price"])
        quantity = int(product_dict["quantity"])

        # * Доп. задание 3: проверка дубликатов по имени
        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, description, price, quantity)
