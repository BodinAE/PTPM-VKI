import unittest
import Converter

class TestConverter(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(Converter.do(200.0), 1000)

    def test_negative(self):
        self.assertEqual(Converter.do(-100.0), -2000)

    def test_boundary_1007(self):
        self.assertEqual(Converter.do(100.7), 1000)

    def test_boundary_neg304(self):
        self.assertEqual(Converter.do(-30.4), -35)

    def test_boundary_neg305(self):
        self.assertEqual(Converter.do(-30.5), -2000)

    def test_positive_less1007(self):
        self.assertEqual(Converter.do(100.6), 100)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Converter.do(0)

if __name__ == '__main__':
    unittest.main()
