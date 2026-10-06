import unittest
from cicle import Circle

class TestCircle(unittest.TestCase):
    def test_circle_initialization(self):
        #Arrange
        circle1 = Circle(5, 0, 0)

        #Act & Assert
        self.assertEqual(circle1._name, "Circle")
        self.assertEqual(circle1._radius, 5)
        self.assertEqual(circle1._x_center, 0)
        self.assertEqual(circle1._y_center, 0)  
        self.assertAlmostEqual(circle1._area, 78.5)

if __name__ == '__main__':
    unittest.main()
