
import re
from day import Day

class Term:

    def __init__(self, hour, minute, duration = 90, day = None):
        self.__duration  = duration
        self.__minute = minute
        self.__hour = hour
        self.__day = day



    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, var):
        self.__hour = var

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, var):
        self.__minute = var

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, var):
        self.__duration = var

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, var):
        self.__day = var



    def __str__(self):
        napis = str(self.hour) + ":" + str(self.minute) + " [" + str(self.duration) + "]"
        return napis


    def earlierThan(self, termin):
        if self.day == None and termin.day == None:
            check1 = [self.hour, self.minute]
            check2 = [termin.hour, termin.minute]
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
        else:
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
        if self.day == None and termin.day == None:
            check1 = [self.hour, self.minute]
            check2 = [termin.hour, termin.minute]
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
        else:
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
        if self.day == None and termin.day == None:
            check1 = [self.hour, self.minute, self.duration]
            check2 = [termin.hour, termin.minute, termin.duration]
            check = 0

            for i in range(len(check1)):
                if check1[i] == check2[i]:
                    check += 1

            if check == 3:
                return True
            return False
        else:
            check1 = [self.day.value, self.hour, self.minute, self.duration]
            check2 = [self.day.value, termin.hour, termin.minute, termin.duration]
            check = 0

            for i in range(len(check1)):
                if check1[i] == check2[i]:
                    check += 1

            if check == 4:
                return True
            return False

    def __lt__(self, other):
        return self.earlierThan(other)

    def __le__(self, other):
        return self.earlierThan(other) or self.equals(other)

    def __gt__(self, other):
        return self.laterThan(other)

    def __ge__(self, other):
        return self.laterThan(other) or self.equals(other)

    def __eq__(self, other):
        return self.equals(other)

    def __sub__(self, other):
        godz = self.duration // 60
        min = self.duration % 60

        end_hour = self.hour + godz + (min + self.minute) // 60
        end_min = (min + self.minute) % 60


        x = Term(other.hour, other.minute)
        x.duration = (end_hour - other.hour)*60 + end_min - other.minute
        return x



'''term1 = Term(Day.TUE, 9, 45)
print(term1)                     # Ma się wypisać: "Wtorek 9:45 [90]"
term2 = Term(Day.WED, 10, 15)
print(term2)                     # Ma się wypisać: "Środa 10:15 [90]"
print(term1.earlierThan(term2)); # Ma się wypisać: "True"
print(term1.laterThan(term2));   # Ma się wypisać: "False"
print(term1.equals(term2));      # Ma się wypisać: "False"'''
