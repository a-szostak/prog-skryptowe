import unittest
from timetable1 import Timetable1
from term import Term
from day import Day
from lesson import Lesson
from action import Action

lesson1 = Lesson(Timetable1, Term(12, 15, day = Day.THU), "Programowanie skryptowe", "Polak", 2)
lesson2 = Lesson(Timetable1, Term(8, 20, day = Day.THU), "Systemy operacyjne", "Rzecki", 2)
lesson3 = Lesson(Timetable1, Term(17, 20, day = Day.FRI), "Kryptografia", "Topa", 2)

table = Timetable1()
table.lessons = [lesson1, lesson2, lesson3]


class TestTimetable1(unittest.TestCase):


    def test_can_be(self):
        self.assertEqual(table.can_be_transferred_to(Term(15, 45, day = Day.THU), True), True)
        self.assertEqual(table.can_be_transferred_to(Term(19, 10, day = Day.FRI), True), False)


    def test_busy(self):
        self.assertEqual(table.busy(Term(15, 45, day = Day.THU)), False)
        self.assertEqual(table.busy(Term(18, 15, day = Day.FRI)), True)


    def test_put(self):
        to_add1 = Lesson(Timetable1, Term(15, 45, day = Day.THU), "Rosyjski", "Jawor", 2)
        to_add2 = Lesson(Timetable1, Term(18, 10, day = Day.FRI), "Rosyjski", "Jawor", 2)

        self.assertEqual(table.put(to_add1), True)
        self.assertEqual(table.put(to_add2), False)

    def test_parse(self):
        self.assertEqual(table.parse(["d-", "aaaaa", "d+", "eeeeeeee", "t-", "t+"]),[Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER])


    def test_perform(self):
        first = Lesson(Timetable1, Term(15, 45, day = Day.THU), "Rosyjski", "Jawor", 2)
        second = Lesson(Timetable1, Term(18, 10, day = Day.WED), "Rosyjski", "Jawor", 2)
        new = Timetable1()
        new.lessons = [first, second]

        actions = table.parse(["d+", "d-", "t+", "t-"])
        new.perform(actions)

        self.assertEqual(first.term.day.value, 5)
        self.assertEqual(first.term.hour, 17)
        self.assertEqual(first.term.minute, 15)
        self.assertEqual(second.term.day.value, 2)
        self.assertEqual(second.term.hour, 16)
        self.assertEqual(second.term.minute, 40)


        actions2 = table.parse(["t+","d-","t-","d-"])
        new.perform(actions2)

        self.assertEqual(second.term.day.value, 1)
        self.assertEqual(first.term.hour, 17)
        self.assertEqual(first.term.minute, 15)

    def test_get(self):
        self.assertEqual(table.get(Term(8, 20, day = Day.THU)), lesson2)
        self.assertEqual(table.get(Term(14, 15, day = Day.THU)), None)


if __name__ == '__main__':
    unittest.main()
