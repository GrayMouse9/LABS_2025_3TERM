class FigureColor:
    """
    Класс для хранения цвета фигуры.
    """
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        """
        Свойство для получения цвета.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Сеттер для установки цвета.
        """
        self._color = value
