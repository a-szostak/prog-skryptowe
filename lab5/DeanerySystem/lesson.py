
from term import Term
from day import Day
from timetable1 import Timetable1
from timetable2 import Timetable2
from b import Break


def check_full_time(term: Term):

    if term.day.value in [1,2,3,4] and (term.hour >= 8 and term.hour < 20):
        return True
    elif term.day.value == 5 and (term.hour >= 8 and term.hour < 17):
        return True
    elif term.day.value in [6,7] and (term.hour >= 8 and term.hour < 20):
        return False
    elif term.day.value == 5 and (term.hour >= 17 and term.hour < 20):
        return False



class Lesson():
    def __init__(self, timetable, term: Term, name: str, teacherName: str, year: int, skipBreaks: bool = True):

        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__full_time = check_full_time(term)
        self.timetable = timetable
        self.skipBreaks = skipBreaks


    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, var):
        self.__term = var

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, var):
        self.__name = var

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, var):
        self.__teacherName = var

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,var):
        self.__year = var

    @property
    def full_time(self):
        return self.__full_time

    @full_time.setter
    def full_time(self, var):
        self.__full_time = var



    def earlierDay(self):
        if check_full_time(self.term) == True and self.term.day.value != 1:
            new_day = self.term.day.value - 1
            new_term = Term(self.term.hour, self.term.minute, day = Day(new_day))



        elif check_full_time(self.term) == False and self.term.day.value != 5:
            new_day = self.term.day.value - 1
            new_term = Term(self.term.hour, self.term.minute, day = Day(new_day))



        else:
            return False

        if self.timetable().can_be_transferred_to(new_term, self.full_time) == True:
            self.term = new_term

        return self.term

    def laterDay(self):
        if check_full_time(self.term) == True and self.term.day.value != 5:
            new_day = self.term.day.value + 1
            new_term = Term(self.term.hour, self.term.minute, day = Day(new_day))


        elif check_full_time(self.term) == False and self.term.day.value != 7:
            new_day = self.term.day.value + 1
            new_term = Term(self.term.hour, self.term.minute, day = Day(new_day))

        else:
            return False

        if self.timetable().can_be_transferred_to(new_term, self.full_time) == True:
            self.term = new_term

        return self.term


    def earlierTime(self):
        if self.skipBreaks == True:

            min = self.term.hour * 60 + self.term.minute
            new_hour = (min - self.term.duration - self.breakBefore) // 60
            new_min = (min - self.term.duration - self.breakBefore) % 60

            new_term = Term(new_hour, new_min, day = self.term.day)

        else:
            min = self.term.hour * 60 + self.term.minute
            new_hour = (min - self.term.duration) // 60
            new_min = (min - self.term.duration) % 60

            new_term = Term(new_hour, new_min, day = self.term.day)

        if self.timetable().can_be_transferred_to(new_term, self.full_time) == True:
            self.term = new_term

            return self.term

        else:
            return False

    def laterTime(self):
        if self.skipBreaks == True:

            min = self.term.hour * 60 + self.term.minute
            new_hour = (self.term.duration + min + self.breakAfter) // 60
            new_min = (self.term.duration + min + self.breakAfter) % 60

            new_term = Term(new_hour, new_min, day = self.term.day)

        else:
            min = self.term.hour * 60 + self.term.minute
            new_hour = (self.term.duration + min ) // 60
            new_min = (self.term.duration + min) % 60

            new_term = Term(new_hour, new_min, day = self.term.day)

        if self.timetable().can_be_transferred_to(new_term, self.full_time) == True:
            self.term = new_term

            return self.term

        else:
            return False


    def __str__(self):
        week = {"1":"Poniedzialek", "2":"Wtorek","3":"Sroda","4":"Czwartek","5":"Piatek","6":"Sobota","7":"Niedziela"}

        godz = self.term.duration // 60
        min = self.term.duration % 60
        end_hour = self.term.hour + godz + (min + self.term.minute) // 60
        end_min = (min + self.term.minute) % 60

        adjectives = {"1":"Pierwszy", "2":"Drugi", "3":"Trzeci", "4":"Czwarty", "5":"Piaty"}
        studies = {"True":"stacjonarnych", "False":"niestacjonarnych"}

        return self.name + " (" + week[str(self.term.day.value)] + " " + str(self.term.hour) \
        + ":" + str(self.term.minute) + " - " + str(end_hour) + ":" + str(end_min) + ")" + "\n" \
        + adjectives[str(self.year)] + " rok studiow " +  studies[str(check_full_time(self.term))]
