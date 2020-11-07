import unittest
from timetable1 import Timetable1
from timetable2 import Timetable2
from b import Break
from term import Term
from day import Day
from lesson import Lesson
from action import Action

lesson1 = Lesson(Timetable2, Term(11, 15, day = Day.THU), "Programowanie", "Polak", 2, True)
lesson2 = Lesson(Timetable2, Term(8, 00, day = Day.WED), "SysOps", "Rzecki", 2, False)
lesson3 = Lesson(Timetable2, Term(12, 50, day = Day.WED), "Kryptografia", "Topa", 2, True)
lesson4 = Lesson(Timetable2, Term(9, 35, day = Day.TUE), "BAWiM", "Juszka", 2, False)

table = Timetable2([Break(Term(9, 30, 5)), Break(Term(11, 5, 10)), Break(Term(12, 45, 5)), Break(Term(14, 20, 20)), Break(Term(16, 10, 5)), Break(Term(17, 45, 5))])
table.lessons = [lesson1, lesson2, lesson3, lesson4]

class TestTimetable2(unittest.TestCase):


    def test_performance(self):
        actions = table.parse(["t-", "t+", "t+", "t-"])
        table.perform(actions)

        self.assertEqual(lesson1.term.hour, 9)
        self.assertEqual(lesson1.term.minute, 35)
        self.assertEqual(lesson2.term.hour, 9)
        self.assertEqual(lesson2.term.minute, 30)
        self.assertEqual(lesson3.term.hour, 14)
        self.assertEqual(lesson3.term.minute, 40)
        self.assertEqual(lesson4.term.hour, 8)
        self.assertEqual(lesson4.term.minute, 5)


    def test_breaks(self):
        self.assertEqual(table.breaks[0].getTerm(), "9:30 - 9:35")
        self.assertEqual(table.breaks[2].getTerm(), "12:45 - 12:50")





if __name__ == '__main__':
    unittest.main()
