import unittest
from basic_shape import BasicShape

class Test_Basic_Shape(unittest.TestCase):
    def test_no_instantiation(self):
        #Arrange
        with self.assertRaises(TypeError):
            Shape1 = BasicShape("Shape1", 10)


if __name__ == '__main__':
    unittest.main()