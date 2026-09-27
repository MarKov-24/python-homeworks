from abc import ABC, abstractmethod
import math


# 1. Абстрактний базовий клас
class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        """Метод для обчислення площі"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Метод для обчислення периметра"""
        pass


# 2. Клас "Квадрат"
class Square(Figure):

    def __init__(self, side: float):
        self.__side = side  # Приватний атрибут

    def area(self) -> float:
        return self.__side**2

    def perimeter(self) -> float:
        return 4 * self.__side


# 3. Клас "Прямокутник"
class Rectangle(Figure):

    def __init__(self, width: float, height: float):
        self.__width = width  # Приватний атрибут
        self.__height = height  # Приватний атрибут

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)


# 4. Клас "Коло"
class Circle(Figure):

    def __init__(self, radius: float):
        self.__radius = radius  # Приватний атрибут

    def area(self) -> float:
        return math.pi * (self.__radius**2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius


# --- Використання класів та обчислення у циклі ---

# Створюємо список із різних об'єктів фігур
figures: list[Figure] = [
    Square(side=5),
    Rectangle(width=4, height=8),
    Circle(radius=3),
]

# Обходимо фігури у циклі та виводимо результати
for figure in figures:
    # Отримуємо назву класу фігури для гарного виводу
    shape_name = figure.__class__.__name__

    print(f"Фігура: {shape_name}")
    print(f"  - Площа: {figure.area():.2f}")
    print(f"  - Периметр: {figure.perimeter():.2f}")
    print("-" * 30)