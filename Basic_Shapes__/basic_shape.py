from abc import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, name: str, area = 0: float)-> None:
        self.name = name
        self.area = area

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @abstractmethod
    def calc_area(self):
        pass




