import unittest
from lesson import Lesson
from term import Term
from day import Day
from timetable1 import Timetable1


class TestLesson(unittest.TestCase):

    def test_earlierDay(self):
        lesson1 = Lesson(Timetable1, Term(12, 50, day = Day.THU), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Timetable1, Term(12, 50, day = Day.MON), "Programowanie skryptowe", "Stanisław Polak", 2)

        self.assertEqual(lesson1.earlierDay().day.value, 3)
        self.assertEqual(lesson2.earlierDay(), False)

    def test_laterDay(self):
        lesson1 = Lesson(Timetable1, Term(12, 50, day = Day.THU), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Timetable1, Term(12, 50, day = Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)

        self.assertEqual(lesson1.laterDay().day.value, 5)
        self.assertEqual(lesson2.laterDay(), False)

    def test_earlierTime(self):
        lesson1 = Lesson(Timetable1, Term(12, 15, day = Day.THU), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Timetable1, Term(8, 20, day = Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson1.earlierTime()

        self.assertEqual(lesson1.term.hour, 10)
        self.assertEqual(lesson1.term.minute, 45)
        self.assertEqual(lesson2.earlierTime(), False)

    def test_laterTime(self):
        lesson1 = Lesson(Timetable1, Term(12, 50, day = Day.THU), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Timetable1, Term(19, 15, day = Day.FRI), "Programowanie skryptowe", "Stanisław Polak", 2)

        lesson1.laterTime()

        self.assertEqual(lesson1.term.hour, 14)
        self.assertEqual(lesson1.term.minute, 20)
        self.assertEqual(lesson2.laterTime(), False)




if __name__ == '__main__':
    unittest.main()
