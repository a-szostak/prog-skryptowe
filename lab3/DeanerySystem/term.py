
import math
from day import Day

class Term:

    def __init__(self, day, hour, minute, duration = 90):
        self.duration  = duration
        self.minute = minute
        self.hour = hour
        self.day = day

    def __str__(self):
        napis = str(self.hour) + ":" + str(self.minute) + " [" + str(self.duration) + "]"
        return napis

    def earlierThan(self, termin):\

        check1 = [self.day.value, self.hour, self.minute]
        check2 = [termin.day.value, termin.hour, termin.minute]
        check = False

        for i in range(len(check1)):
            if check1[i] < check2[i]:
                check = True
                break
            elif check1[i] == check2[i]:
                continue
            else:
                break

        return check


    def laterThan(self, termin):
        check1 = [self.day.value, self.hour, self.minute]
        check2 = [termin.day.value, termin.hour, termin.minute]
        check = False

        for i in range(len(check1)):
            if check1[i] > check2[i]:
                check = True
                break
            elif check1[i] == check2[i]:
                continue
            else:
                break

        return check

    def equals(self, termin):

        check1 = [self.day.value, self.hour, self.minute]
        check2 = [termin.day.value, termin.hour, termin.minute]
        check = 0

        for i in range(len(check1)):
            if check1[i] == check2[i]:
                check += 1

        if check == 3:
            return True
        return False

    def difference(self, termin):
        return Diff(self, termin)


class Diff():
    def __init__(self, term1, term2):
        self.days = term1.day.difference(term2.day)

        min1 = term1.minute + term1.hour*60 + (term1.day.value - 1) * 24 *60
        min2 = term2.minute + term2.hour*60 + (term2.day.value - 1) * 24 * 60
        self.minutes = math.fabs(min1 - min2)

        self.hours = self.minutes // 60

        self.seconds = self.minutes * 60




'''term1 = Term(Day.TUE, 9, 45)
print(term1)                     # Ma się wypisać: "Wtorek 9:45 [90]"
term2 = Term(Day.WED, 10, 15)
print(term2)                     # Ma się wypisać: "Środa 10:15 [90]"
print(term1.earlierThan(term2)); # Ma się wypisać: "True"
print(term1.laterThan(term2));   # Ma się wypisać: "False"
print(term1.equals(term2));      # Ma się wypisać: "False"'''
