import leap_year_2
import unittest

class testLeap(unittest.TestCase):
    def test1(self):
        self.assertEqual(leap_year_2.leap_year(400), "That is a leap year")
        self.assertEqual(leap_year_2.leap_year(401), "That is not a leap year")


if __name__ == '__main__':
    unittest.main()