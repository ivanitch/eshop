class ZeroQuantityError(ValueError):
    """Исключение, которое вызывается при попытке добавить товар с нулевым количеством."""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        super().__init__(message)
