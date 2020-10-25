import unittest, term
from term import Term
from day import Day

term1 = Term(Day.TUE, 9, 45)
term2 = Term(Day.WED, 10, 15)

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_earlier(self):
        self.assertEqual(term1.earlierThan(term2), True)

    def test_later(self):
        self.assertEqual(term1.laterThan(term2), False)

    def test_equals(self):
        self.assertEqual(term1.equals(term2), False)



if __name__ == '__main__':
    unittest.main()
