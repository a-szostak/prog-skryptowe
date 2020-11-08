import unittest
from timetable1 import Timetable1
from term import Term
from day import Day
from lesson import Lesson
from action import Action
from basic import BasicTerm
from basicTimetable import BasicTimetable


lesson1 = Lesson(Timetable1, Term(12, 15, day = Day.THU), "Programowanie", "Polak", 2)
lesson2 = Lesson(Timetable1, Term(12, 15, day = Day.THU), "SysOps", "Rzecki", 2)
table = Timetable1()


class TestExceptions(unittest.TestCase):

    def test_parse(self):
        #self.assertRaises(ValueError, lambda: table.parse(["d-", "d+", "sth_else", "t-", "t+"]))
        table.parse(["d-", "d+", "sth_else", "t-", "t+"])


    def test_put(self):
        table.put(lesson1)
        #table.put(lesson2)
        #self.assertEqual(table.put(lesson2), "This term is busy")




lesson1 = Lesson(Timetable1, Term(12, 15, day = Day.THU), "Programowanie", "Polak", 2)
lesson2 = Lesson(Timetable1, Term(12, 15, day = Day.THU), "SysOps", "Rzecki", 2)
table = Timetable1()
table.parse(["d-", "d+", "sth_else", "t-", "t+"])













if __name__ == '__main__':
    unittest.main()
