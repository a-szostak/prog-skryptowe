from typing import List
from term import Term
from lesson2 import Lesson
from action import Action
from day import Day
import math

class Timetable1:
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        self.lessons = []

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

        for lesson in self.lessons:
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

        for lesson in self.lessons:
            if lesson.term.day == term.day:
                lesson_start = lesson.term.hour * 60 + lesson.term.minute
                lesson_end = lesson_start + lesson.term.duration

                if (term_start >= lesson_start and term_start <= lesson_end) or (term_end >= lesson_start and term_end <= lesson_end):
                    check = True
                    break
        return check

 ##########################################################

    def put(self, lesson: Lesson) -> bool:
        """
Add the given lesson to the timetable.

Parameters
----------
lesson : Lesson
    The added  lesson

Returns
-------
bool
    **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """

        if self.can_be_transferred_to(lesson.term, lesson.full_time) == True:
            self.lessons.append(lesson)
            return True
        return False


##########################################################

    def parse(self, actions: List[str]) -> List[Action]:
        """
Converts an array of strings to an array of 'Action' objects.

Parameters
----------
actions:  List[str]
    A list containing the strings: "d-", "d+", "t-" or "t+"

Returns
-------
    List[Action]
        A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """

        list_action = []

        for action in actions:
            if action == "d-":
                list_action.append(Action.DAY_EARLIER)
            elif action == "d+":
                list_action.append(Action.DAY_LATER)
            elif action == "t-":
                list_action.append(Action.TIME_EARLIER)
            elif action == "t+":
                list_action.append(Action.TIME_LATER)

        return list_action

##########################################################

    def perform(self, actions: List[Action]):
        """
Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

Parameters
----------
actions : List[Action]
    Actions to be performed
        """

        number = 0

        for action in actions:
            if action == Action.DAY_EARLIER:
                self.lessons[number].earlierDay()
            elif action == Action.DAY_LATER:
                self.lessons[number].laterDay()
            elif action == Action.TIME_EARLIER:
                self.lessons[number].earlierTime()
            elif action == Action.TIME_LATER:
                self.lessons[number].laterTime()
            number = (number + 1) % len(self.lessons)
##########################################################

    def get(self, term: Term) -> Lesson:
        """
Get object (lesson) indicated by the given term.

Parameters
----------
term: Term
    Lesson date

Returns
-------
lesson: Lesson
    The lesson object or None if the term is free
        """

        for lesson in self.lessons:
            if lesson.term == term:
                return lesson
        return None


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
            for lesson in self.lessons:

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
