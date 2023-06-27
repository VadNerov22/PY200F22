import math
from typing import Union


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """
    def __init__(self, side_a: Union[int, float], side_b: Union[int, float]):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return self.side_a * self.side_b


class Circle(Figure):
    """ Производный класс. Круг. """
    def __init__(self, r: Union[int, float]):
        self.r = r

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return 2 * math.pi * (self.r ** 2)


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
