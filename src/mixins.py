class LogMixin:
    """Миксин: при создании объекта выводит имя класса и его параметры."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" f"{self.name!r}, {self.description!r}, " f"{self.price}, {self.quantity})"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))
