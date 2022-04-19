import unittest
import calc



class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 7), 10)


    def test_is_positive(self):
        self.assertTrue(calc.is_positive(3))


    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            calc.divide(8, 0)


    def test_upper(self):
        self.assertEqual('abc'.upper(), 'ABC')

    def test_islower(self):
        self.assertEqual('abc'.islower(), True)

    def test_count(self):
        self.assertEqual('abc'.count('a'), 1)



if __name__ == "__main__":
    unittest.main()

