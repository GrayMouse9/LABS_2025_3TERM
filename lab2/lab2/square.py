from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    """
    Класс для представления квадрата, наследуется от Прямоугольника.
    """
    name = "Квадрат"

    def __init__(self, side, color):
        # Вызываем конструктор родительского класса (Rectangle)
        super().__init__(side, side, color)
        self.side = side

    def __repr__(self):
        return "Фигура: {}. Сторона: {}. Цвет: {}. Площадь: {}.".format(
            self.get_name(),
            self.side,
            self.figure_color.color,
            self.calculate_area()
        )

    @classmethod
    def get_name(cls):
        return cls.name
