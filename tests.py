import unittest
import calc



class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 7), 10)


    def test_is_positive(self):
        self.assertTrue(calc.is_positive(3))


if __name__ == "__main__":
    unittest.main()
