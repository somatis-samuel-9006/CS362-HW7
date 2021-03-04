import leap_year_2
import unittest

class testLeap(unittest.TestCase):
    #divisible by 4 or not
    def test1(self):
        self.assertEqual(leap_year_2.leap_year(400), "That is a leap year")
        self.assertEqual(leap_year_2.leap_year(401), "That is not a leap year")
    #divisible by 4 and 100. includes test for div by 4 by not by 100
    def test2(self):
        self.assertEqual(leap_year_2.leap_year(400), "That is a leap year")
        self.assertEqual(leap_year_2.leap_year(12), "That is a leap year")
    #divisible by 4 and 100 and 400. includes test for div by 4 and 100, but not by 400
    def test3(self):
        self.assertEqual(leap_year_2.leap_year(400), "That is a leap year")
        self.assertEqual(leap_year_2.leap_year(200), "That is not a leap year")

if __name__ == '__main__':
    unittest.main()