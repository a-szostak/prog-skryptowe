from term import Term
from day import Day
from typing import List
from lesson2 import Lesson
from b import Break
from basic import BasicTerm
from basicTimetable import BasicTimetable
from action import Action

class Timetable2(BasicTimetable):

    def __init__(self, breaks: List[Break] = None):
        self.breaks = breaks
        self.lessons = []

    '''def __init__(self):
        self.breaks = [Break(Term(9, 30, 5)), Break(Term(11, 5, 10))]
        self.lessons = []'''



    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if full_time != check_full_time(term):
            return False

        term_start = term.hour * 60 + term.minute
        term_end = term_start + term.duration

        check = True

        for lesson in self.lessons:
            if lesson.term.day == term.day:
                lesson_start = lesson.term.hour * 60 + lesson.term.minute
                lesson_end = lesson_start + lesson.term.duration

                if (term_start >= lesson_start and term_start <= lesson_end) or (term_end >= lesson_start and term_end <= lesson_end):
                    check = False
                    break
        return check


    def busy(self, term: Term) -> bool:
        term_start = term.hour * 60 + term.minute
        term_end = term_start + term.duration

        check = False

        for lesson in self.lessons:
            if lesson.term.day == term.day:
                lesson_start = lesson.term.hour * 60 + lesson.term.minute
                lesson_end = lesson_start + lesson.term.duration

                if (term_start >= lesson_start and term_start <= lesson_end) or (term_end >= lesson_start and term_end <= lesson_end):
                    check = True
                    break
        return check


    def put(self, lesson: Lesson):
        super().put(lesson)
        self.att_setter()

    def perform(self, actions: List[Action]):
        self.att_setter()
        super().perform(actions)
        self.att_setter()


    def which_break(self, lesson: Lesson):
        for b in self.breaks:
            lesson_end = lesson.term.hour * 60 + lesson.term.minute + lesson.term.duration
            break_start = b.term.hour *60 + b.term.minute
            if b.end_hr == lesson.term.hour and b.end_min == lesson.term.minute:
                setattr(lesson, 'breakBefore', b.term.duration)
                #lesson.breakBefore = b.term.duration
            elif lesson_end == break_start:
                setattr(lesson, 'breakAfter', b.term.duration)
                lesson.breakAfter = b.term.duration


    def att_setter(self):
        for lesson in self.lessons:
            self.which_break(lesson)



    def __str__(self):
        print(" " * 12, "*Poniedziałek*Wtorek     *Środa      *Czwartek    *Piątek      *Sobota    *Niedziela")
        print(" " * 12, "*" * 84)
        godziny = {
        "8": "8:00-9:30",
        "9": "9:35-11:05",
        "11": "11:15-12:45",
        "12": "12:50-14:20",
        "14": "14:40-16:10",
        "15": "16:15-17:45",
        "17": "17:50-19:20",
        }

        przerwy = [
        "9:30-9:35",
        "11:05-11:15",
        "12:45-12:50",
        "14:20-14:40",
        "16:10-16:15",
        "17:45-17:50"
        ]
        j = 0
        for i in godziny:


            #print(" " * 12, "*" * 84)
            print(" "*12)
            wiersz = [" "*13, "*", " "*12 , "*" , " "*11 , "*" , " "*11 , "*" , " "*12 , "*" , " "*12 , "*" , " "*10 , "*"]
            #print("             *           *              *           *         *        *")
            for lesson in self.lessons:

                if lesson.term.hour == int(i):
                    index = 2 * lesson.term.day.value
                    #len(wiersz[index])
                    wiersz[index] = lesson.name + " "*(len(wiersz[index]) - len(lesson.name))
            print("".join(wiersz))
            print (godziny[i] + "\n\n")
            print(przerwy[j] + "  " + "-"*84 + "\n")
            if j < 5:
                j += 1
            print(" " * 12, "*" * 84)

        return ""


def check_full_time(term: Term):

    if term.day.value in [1,2,3,4] and (term.hour >= 8 and term.hour < 20):
        return True
    elif term.day.value == 5 and (term.hour >= 8 and term.hour < 17):
        return True
    elif term.day.value in [6,7] and (term.hour >= 8 and term.hour < 20):
        return False
    elif term.day.value == 5 and (term.hour >= 17 and term.hour < 20):
        return False
