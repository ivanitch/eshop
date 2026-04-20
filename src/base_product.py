from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение стоимостей двух продуктов."""
        pass


class BaseEntityWithStr(ABC):
    """Общий абстрактный класс для сущностей, которые умеют представляться строкой."""

    @abstractmethod
    def __str__(self) -> str:
        pass
