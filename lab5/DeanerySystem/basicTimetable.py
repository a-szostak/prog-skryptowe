from term import Term
from lesson2 import Lesson
from basic import BasicTerm
from typing import List
from action import Action
#from day import Day


class BasicTimetable:

    def __init__(self):
        pass

    def get(self, term: Term) -> Lesson:
        for lesson in self.lessons:
            if lesson.term == term:
                return lesson
        return None

    def parse(self, actions: List[str]) -> List[Action]:
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
            else:
                raise ValueError("Translation " + action + " is incorrect")

        return list_action

    def perform(self, actions: List[Action]):
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




    def put(self, lesson: Lesson) -> bool:

        if self.can_be_transferred_to(lesson.term, lesson.full_time) == True:
            self.lessons.append(lesson)
            return True
        return False
