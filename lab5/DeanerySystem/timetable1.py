from typing import List
from term import Term
from lesson2 import Lesson
from action import Action
from day import Day
from basic import BasicTerm
from basicTimetable import BasicTimetable
import math

class Timetable1(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        self.lessons = {}

##########################################################
    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        """
Informs whether a lesson can be transferred to the given term

Parameters
----------
term : Term
    The term checked for the transferability
full_time : bool
    Full-time or part-time studies

Returns
-------
bool
    **True** if the lesson can be transferred to this term
"""
        if full_time != check_full_time(term):
            return False

        term_start = term.hour * 60 + term.minute
        term_end = term_start + term.duration

        check = True

        for lesson in self.lessons.values():
            if lesson.term.day == term.day:
                lesson_start = lesson.term.hour * 60 + lesson.term.minute
                lesson_end = lesson_start + lesson.term.duration

                if (term_start >= lesson_start and term_start <= lesson_end) or (term_end >= lesson_start and term_end <= lesson_end):
                    check = False
                    break
        return check




##########################################################

    def busy(self, term: Term) -> bool:
        """
Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
since there might be free term where the lesson cannot be transferred.

Parameters
----------
term : Term
    Checked term

Returns
-------
bool
    **True** if the term is busy
        """

        term_start = term.hour * 60 + term.minute
        term_end = term_start + term.duration

        check = False

        for lesson in self.lessons.values():
            if lesson.term.day == term.day:
                lesson_start = lesson.term.hour * 60 + lesson.term.minute
                lesson_end = lesson_start + lesson.term.duration

                if (term_start >= lesson_start and term_start <= lesson_end) or (term_end >= lesson_start and term_end <= lesson_end):
                    check = True
                    break
        return check



    def __str__(self):
        print(" " * 12, "*Poniedziałek*Wtorek     *Środa      *Czwartek    *Piątek      *Sobota    *Niedziela")
        print(" " * 12, "*" * 84)
        godziny = {
        "8": "8:00-8:30",
        "9": "9:30-11:00",
        "11": "11:00-12:30",
        "12": "12:30-14:00",
        "14": "14:00-15:30",
        "15": "15:30-17:00",
        "17": "17:00-18:30",
        "18": "18:30-20:00"}

        for i in godziny:


            #print(" " * 12, "*" * 84)
            print(" "*12)
            wiersz = [" "*13, "*", " "*12 , "*" , " "*11 , "*" , " "*11 , "*" , " "*12 , "*" , " "*12 , "*" , " "*10 , "*"]
            #print("             *           *              *           *         *        *")
            for lesson in self.lessons.values():

                if lesson.term.hour == int(i):
                    index = 2 * lesson.term.day.value
                    #len(wiersz[index])
                    wiersz[index] = lesson.name + " "*(len(wiersz[index]) - len(lesson.name))
            print("".join(wiersz))
            print (godziny[i])
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
