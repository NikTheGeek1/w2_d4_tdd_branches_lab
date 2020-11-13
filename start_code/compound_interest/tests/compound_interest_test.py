import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_100_10_20_return_732comma81(self):
        interest = CompoundInterest(100, .1, 20)
        self.assertEqual(732.81, interest.calculator())

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_100_6_10_return_181comma94(self): 
        interest = CompoundInterest(100, .06, 10)
        self.assertEqual(181.94, interest.calculator())

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_10000_5_8_return_149085comma55(self):
        self.assertEqual(149058.55, CompoundInterest(100000, .05, 8).calculator())

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test4(self):
        self.assertEqual(0.0, CompoundInterest(0, .1, 1).calculator())
    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test5(self):
        self.assertEqual(118380.16, CompoundInterest(100, .05, 8, 1000).calculator_with_contributions())
    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    def test6(self):
        self.assertEqual(156093.99, CompoundInterest(100, 0.05, 10, 1000).calculator_with_contributions())
    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    def test7(self):
        self.assertEqual(475442.59, CompoundInterest(116028.86, 0.075, 8, 2006).calculator_with_contributions())
    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
    def test8(self):
        self.assertEqual(718335.97, CompoundInterest(116028.86, 0.09, 12, 1456).calculator_with_contributions())
