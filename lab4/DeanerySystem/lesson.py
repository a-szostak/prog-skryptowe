
from term import Term
from day import Day

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
    def __init__(self, term: Term, name: str, teacherName: str, year: int):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = check_full_time(term)

    def earlierDay(self):
        if check_full_time(self.term) == True and self.term.day.value != 1:
            new_day = self.term.day.value - 1
            self.term= Term(self.term.hour, self.term.minute, day = Day(new_day))


        elif check_full_time(self.term) == False and self.term.day.value != 5:
            new_day = self.term.day.value - 1
            self.term = Term(self.term.hour, self.term.minute, day = Day(new_day))
            

        else:
            return False

        return self.term

    def laterDay(self):
        if check_full_time(self.term) == True and self.term.day.value != 5:
            new_day = self.term.day.value + 1
            self.term = Term(self.term.hour, self.term.minute, day = Day(new_day))


        elif check_full_time(self.term) == False and self.term.day.value != 7:
            new_day = self.term.day.value + 1
            self.term = Term(self.term.hour, self.term.minute, day = Day(new_day))

        else:
            return False

        return self.term


    def earlierTime(self):
        min = self.term.hour * 60 + self.term.minute
        new_hour = (min - self.term.duration) // 60
        new_min = (min - self.term.duration) % 60

        self.term = Term(new_hour, new_min, day = self.term.day)

        if check_full_time(self.term) != None:
            return self.term
        else:
            return False

    def laterTime(self):
        min = self.term.hour * 60 + self.term.minute
        new_hour = (self.term.duration + min) // 60
        new_min = (self.term.duration + min) % 60

        self.term = Term(new_hour, new_min, day = self.term.day)

        if check_full_time(self.term) != None:
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
