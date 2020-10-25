
#!/bin/bash env python3

import math
from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7


    def difference(self, day):
        if self.value > day.value:
            wynik1 = self.value - day.value
            wynik2 = (self.value + day.value) % 7 * 

            if wynik1 < wynik2:
                return wynik1
            else:
                return wynik2

        else:
            wynik1 = day.value - self.value
            wynik2 = (self.value + day.value) % 7 * -1
            if math.fabs(wynik1) < math.fabs(wynik2):
                return wynik1
            else:
                return wynik2

        #return wynik


def nthDayFrom(n, day):
    wynik = (day.value + n) % 7

    if wynik == 0:
        wynik = 7

    return Day(wynik)
