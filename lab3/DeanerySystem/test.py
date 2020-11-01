import unittest, term
from term import Term, Diff
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


class TestTerm(unittest.TestCase):
    def setUp(self):
        self.term1 = Term(Day.TUE, 9, 45)
        self.term2 = Term(Day.WED, 10, 15)

    def test_difference(self):
        diff = self.term1.difference(self.term2)
        self.assertIsInstance(diff, Diff)
        self.assertEqual(diff.seconds, 88_200)
        self.assertEqual(diff.minutes, 1_470)
        self.assertEqual(diff.hours, 24) #wartosc zaokraglona w dol
        self.assertEqual(diff.days, 1)

if __name__ == '__main__':
    unittest.main()
