import unittest
from basic_shape import BasicShape
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_initialization(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        self.assertEqual(rectangle1._name, "Rectangle")
        self.assertEqual(rectangle1._length, 5)
        self.assertEqual(rectangle1._width, 10)
        self.assertAlmostEqual(rectangle1._area, 50.0)

   """ def test_zero_length(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        with self.assertRaises(ValueError):
            rectangle1.length = 0

    def test_negative_length(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        with self.assertRaises(ValueError):
            rectangle1.length = -5

    def test_nonnumeric_length(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        with self.assertRaises(TypeError):
            rectangle1.length = "five"

    def test_zero_width(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        with self.assertRaises(ValueError):
            rectangle1.width = 0

    def test_negative_width(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        with self.assertRaises(ValueError):
            rectangle1.width = -10

    def test_nonnumeric_width(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")

        #Act & Assert
        with self.assertRaises(TypeError):
            rectangle1.width = "ten"

    def test_area_recalculation(self):
        #Arrange
        rectangle1 = Rectangle(5, 10, "Rectangle")
        
        #Act
        self.assertAlmostEqual(rectangle1._area, 50.0)
        rectangle1.length = 8
        rectangle1.width = 6
        
        #Assert
        self.assertEqual(rectangle1._length, 8)
        self.assertEqual(rectangle1._width, 6)
        self.assertAlmostEqual(rectangle1._area, 48.0)"""


if __name__ == '__main__':
    unittest.main()