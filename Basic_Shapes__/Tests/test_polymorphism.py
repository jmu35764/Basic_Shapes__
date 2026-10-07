import unittest
from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square

class Test_Polymorphism(unittest.TestCase):
    def test_polymorphism(self):
        #Arrange
        circle1 = Circle(5, 0, 0)
        rectangle1 = Rectangle(5, 10, "Rectangle")
        square1 = Square(5, "Square")
        #Act & Assert
        self.assertIsInstance(circle1, BasicShape)
        self.assertIsInstance(rectangle1, BasicShape)
        self.assertIsInstance(square1, BasicShape)

if __name__ == '__main__':
    unittest.main()
