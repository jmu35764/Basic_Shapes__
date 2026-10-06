from basic_shape import BasicShape

class Circle(BasicShape):
    def __init__(self, _name, r:float, x:int, y:int, n: str = "Circle"):
        super().__init__(_name)
        self._radius = r
        self._x_center = x
        self._y_center = y
        self._name = n
        self._area = self.calc_area()



    def calc_area(self):
        self._area = 3.14 * (self._radius ** 2)
        return self._area

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number")
        if value <= 0:
            raise ValueError("Radius must be a positive number")
        self._radius = value
        self._area = self.calc_area()

    @property
    def x_center(self):
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        if not isinstance(value, int):
            raise TypeError("x_center must be a number")
        self._x_center = value

    @property
    def y_center(self):
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        if not isinstance(value, int):
            raise TypeError("y_center must be a number")
        self._y_center = value


