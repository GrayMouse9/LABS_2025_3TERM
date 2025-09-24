import math
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.figure_color import FigureColor

class Circle(GeometricFigure):
    """
    Класс для представления круга.
    """
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.figure_color = FigureColor(color)

    def calculate_area(self):
        """
        Вычисляет площадь круга.
        """
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "Фигура: {}. Радиус: {}. Цвет: {}. Площадь: {:.2f}.".format(
            self.get_name(),
            self.radius,
            self.figure_color.color,
            self.calculate_area()
        )

    @classmethod
    def get_name(cls):
        return cls.name
